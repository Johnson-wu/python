#coding:utf-8

import subprocess,pexpect
import datetime,time
import re,os
import threading
from constant import *
import logging

def generate_filename(date, identifier):
	# return date + '_' + identifier + '.dmp'
	return date + '_' + identifier + '.gz' 

# 首先查看数据库是否被占用，若是则先杀进程，然后再更新数据库
def kill_process(name, role='postgres'):
	ps = subprocess.Popen('ps -ef|grep %s' % name,shell=True,stdout=subprocess.PIPE)
	ps_result = ps.stdout.read()
	if role in ps_result:
		proc_list = re.split(r'\n',ps_result)  # 匹配换行符
		for proc in proc_list:
			if role in proc:
				pid = proc.split()[1]
				subprocess.check_call('kill -9 %s' % pid,shell=True)


# 数据库备份：每天中午1点，晚上23点这两个时段对数据库进行备份。备份的文件名由 日期、所在单位标识 组成
def dump_db(identifier, db_name, backup_path, db_address=LOCALHOST, loger=None):
	while True:
		date = datetime.datetime.now().strftime('%Y%m%d%H')
		try:
			if len(os.listdir(backup_path)) > 3 and date[6:8] == '21' and date[8:] == '13':
					# ls后面接路径不起作用，所以分成两个命令，先进到备份目录，然后匹配以7个字母或数字开头，并且第7位是0或1的所有文件。
					# "|xargs" 是将前面的命令当参数传递给rm,并执行rm
					subprocess.check_call('cd %s && ls |grep "^\w\{6\}[01]"|xargs rm -f' % backup_path,shell=True)
				
			dmp_name = generate_filename(date,identifier)
			#print(date)
			if date[8:] in ('13','23') and not os.path.exists(backup_path + '/' + dmp_name):
				print(date[8:])
				# subprocess.check_call('%s/pg_dump -i -h %s -p %s -U %s %s > %s/%s' % (PGDUMP_CMD_PATH,LOCALHOST,PORT,DB_USER,DB_NAME,BACKUP_PATH,dmp_name),shell=True)
				subprocess.check_call('%s/pg_dump -i -h %s -p %s -U %s %s|gzip > %s/%s' % (PGDUMP_CMD_PATH,db_address,PORT,DB_USER,db_name,backup_path,dmp_name),shell=True)
				if identifier == HT_IDENT:
					# 备份完成后，复制一份到WAIT_TRANS_PATH目录中
					subprocess.check_call('cp %s/%s %s/%s' % (backup_path,dmp_name,WAIT_TRANS_PATH,dmp_name),shell=True)
				elif identifier == CENTER_IDENT:
					subprocess.check_call('cp %s/%s %s/%s' % (backup_path,dmp_name,CENTER_TRANS_PATH,dmp_name),shell=True)
			else:
				pass
		except Exception, e:
			print e		
			loger.exception(e)
		time.sleep(60)


# 每天中午13点，晚上23点这两个时段，对数据库进行更新。在更新前检查数据库是否被占用，如果是则杀掉相应进程，然后再更新。
def update_db(update_path, backup_path, db_name, db_address=LOCALHOST, loger=None):
	while True:
		try:
			date = datetime.datetime.now().strftime('%Y%m%d%H')
			if date[8:] in ('13','23'):
				# 查找waiting_update目录，如果有文件，则更新。否则，continue
				filelist = os.listdir(update_path)
				if len(filelist) > 0:
					# 有待更新文件，先复制一份到BACKUP_PATH,做为备份
					subprocess.check_call('cp %s/%s %s/%s' % (update_path,filelist[0],backup_path,filelist[0]),shell=True)
					# 杀掉占用数据库的进程
					kill_process(db_name)
					# 更新数据库
					print ('drop db %s' % db_name)
					child_drop = pexpect.spawn('%s/dropdb -i -h %s -p %s -U %s %s' % (PGDUMP_CMD_PATH,LOCALHOST,PORT,DB_USER,db_name))
					expect_str = 'Database "' + db_name + '" will be permanently removed.'
					expect_str2 = 'database "' + db_name + '" does not exist'
					result_code = child_drop.expect([expect_str,expect_str2])
					if result_code == 0:
						child_drop.sendline('yes')
						child_drop.expect(pexpect.EOF)
					elif result_code == 1:
						pass

					kill_process('template1')
					subprocess.check_call('%s/createdb -h %s -p %s -U %s %s' % (PGDUMP_CMD_PATH,LOCALHOST,PORT,DB_USER,db_name),shell=True)

					subprocess.check_call('gunzip -c %s/%s | %s/psql -h %s -p %s -U %s %s' % (update_path,filelist[0],PGDUMP_CMD_PATH,LOCALHOST,PORT,DB_USER,db_name), shell=True)
					# 更新完成，清空待更新目录
					subprocess.check_call('rm -f %s' % update_path + '/*',shell=True)
				else:
					pass
			else:
				pass
		except Exception,e:
			print e
			loger.exception(e)
		time.sleep(60)



if __name__ == '__main__':
	FORMAT = '%(asctime)s - %(levelname)s - %(module)s : %(message)s'
    logging.basicConfig(filename='db_operation.log',format=FORMAT)
    loger = logging.getLogger('root') 
	
	# args: identifier, db_name, backup_path
	# 会同数据库备份，同时会保存一份到中心
	# threading.Thread(target=dump_db,args=(HT_IDENT, DB_NAME, BACKUP_PATH)).start()
	# 平台数据库备份，暂时不保存一份到其他主机
	threading.Thread(target=dump_db,args=(CENTER_IDENT, DB_NAME, CENTER_BACKUP_PATH, LOCALHOST, loger)).start()

	# args: update_path, backup_path, db_name
	# 启动保存在平台的会同数据库镜像的更新
	threading.Thread(target=update_db,args=(WAIT_UPDATE_PATH, BACKUP_PATH, CENTER_BACKUP_DB_NAME, LOCALHOST, loger)).start()
