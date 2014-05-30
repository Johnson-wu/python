#coding:utf-8

import subprocess,pexpect
import datetime,time as timer
import re,os
import threading
from constant import *

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
				subprocess.call('kill -9 %s' % pid,shell=True)


# 基层数据库备份：每天中午1点，晚上23点这两个时段对数据库进行备份。备份的文件名由 日期、所在单位标识 组成
def dump_db():
	while True:
		date = datetime.datetime.now().strftime('%Y%m%d%H')

		if len(os.listdir(BACKUP_PATH)) > 3 and date[6:8] == '21' and date[8:] == '13':
				# ls后面接路径不起作用，所以分成两个命令，先进到备份目录，然后匹配以7个字母或数字开头，并且第7位是0或1的所有文件。
				# "|xargs" 是将前面的命令当参数传递给rm,并执行rm
				subprocess.call('cd %s && ls |grep "^\w\{6\}[01]"|xargs rm -f' % BACKUP_PATH,shell=True)
			
		dmp_name = generate_filename(date,HT_IDENT)
		#print(date)
		if date[8:] in ('13','23') and not os.path.exists(BACKUP_PATH + '/' + dmp_name):
			print(date[8:])
			# subprocess.call('%s/pg_dump -i -h %s -p %s -U %s %s > %s/%s' % (PGDUMP_CMD_PATH,LOCALHOST,PORT,DB_USER,DB_NAME,BACKUP_PATH,dmp_name),shell=True)
			subprocess.call('%s/pg_dump -i -h %s -p %s -U %s %s|gzip > %s/%s' % (PGDUMP_CMD_PATH,LOCALHOST,PORT,DB_USER,DB_NAME,BACKUP_PATH,dmp_name),shell=True)
			# 备份完成后，复制一份到WAIT_TRANS_PATH目录中
			subprocess.call('cp %s/%s %s/%s' % (BACKUP_PATH,dmp_name,WAIT_TRANS_PATH,dmp_name),shell=True)
		else:
			continue
		timer.sleep(60)


# 中心数据库备份
def center_dump_db():
	while True:
		date = datetime.datetime.now().strftime('%Y%m%d%H')

		if len(os.listdir(CENTER_BACKUP_PATH)) > 3 and date[6:8] == '21' and date[8:] == '13':
				# ls后面接路径不起作用，所以分成两个命令，先进到备份目录，然后匹配以7个字母或数字开头，并且第7位是0或1的所有文件。
				# "|xargs" 是将前面的命令当参数传递给rm,并执行rm
				subprocess.call('cd %s && ls |grep "^\w\{6\}[01]"|xargs rm -f' % CENTER_BACKUP_PATH,shell=True)
			
		dmp_name = generate_filename(date,CENTER_IDENT)

		if date[8:] in ('13','23') and not os.path.exists(CENTER_BACKUP_PATH + '/' + dmp_name):
			# subprocess.call('%s/pg_dump -i -h %s -p %s -U %s %s > %s/%s' % (PGDUMP_CMD_PATH,LOCALHOST,PORT,DB_USER,DB_NAME,BACKUP_PATH,dmp_name),shell=True)
			subprocess.call('%s/pg_dump -i -h %s -p %s -U %s %s|gzip > %s/%s' % (PGDUMP_CMD_PATH,LOCALHOST,PORT,DB_USER,DB_NAME,CENTER_BACKUP_PATH,dmp_name),shell=True)
		else:
			continue
		timer.sleep(60)


# 每天中午13点，晚上23点这两个时段，对数据库进行更新。在更新前检查数据库是否被占用，如果是则杀掉相应进程，然后再更新。
def update_db():
	while True:
		date = datetime.datetime.now().strftime('%Y%m%d%H')
		if date[8:] in ('13','23'):
			# 查找waiting_update目录，如果有文件，则更新。否则，continue
			filelist = os.listdir(WAIT_UPDATE_PATH)
			if len(filelist) > 0:
				# 有待更新文件，先复制一份到BACKUP_PATH,做为备份
				subprocess.call('cp %s/%s %s/%s' % (WAIT_UPDATE_PATH,filelist[0],BACKUP_PATH,filelist[0]),shell=True)
				# 杀掉占用数据库的进程
				kill_process(DB_NAME)
				# 更新数据库
				child_drop = pexpect.spawn('%s/dropdb -i -h %s -p %s -U %s %s' % (PGDUMP_CMD_PATH,LOCALHOST,PORT,DB_USER,DB_NAME))
				expect_str = 'Database "' + DB_NAME + '" will be permanently removed.'
				expect_str2 = 'database "' + DB_NAME + '" does not exist'
				result_code = child_drop.expect([expect_str,expect_str2])
				if result_code == 0:
					child_drop.sendline('yes')
					child_drop.expect(pexpect.EOF)
				elif result_code == 1:
					pass

				kill_process('template1')
				subprocess.call('%s/createdb -h %s -p %s -U %s %s' % (PGDUMP_CMD_PATH,LOCALHOST,PORT,DB_USER,DB_NAME),shell=True)
				# child_create = pexpect.spawn('%s/createdb -h %s -p %s -U %s %s' % (PGDUMP_CMD_PATH,LOCALHOST,PORT,DB_USER,DB_NAME))
				# result_code = child_create.expect('source database "template1" is being accessed by other users')

				# subprocess.call('%s/psql -h %s -p %s -U %s %s < %s/%s' % (PGDUMP_CMD_PATH,LOCALHOST,PORT,DB_USER,DB_NAME,WAIT_UPDATE_PATH,filelist[0]), shell=True)
				subprocess.call('gunzip -c %s/%s | %s/psql -h %s -p %s -U %s %s' % (WAIT_UPDATE_PATH,filelist[0],PGDUMP_CMD_PATH,LOCALHOST,PORT,DB_USER,DB_NAME), shell=True)
				# 更新完成，清空待更新目录
				subprocess.call('rm -f %s' % WAIT_UPDATE_PATH + '/*',shell=True)
			else:
				continue
		else:
			continue
		timer.sleep(60)




threading.Thread(target=dump_db,args=()).start()
# threading.Thread(target=center_dump_db,args=()).start()
# threading.Thread(target=update_db,args=()).start()
