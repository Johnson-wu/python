#coding:utf-8

import subprocess,threading
import pexpect
import datetime,os,time
from constant import *
import logging

def transfer_dmp(from_path,to_path,remote_user,remote_pwd,remote_addr,loger):
	while True:
		try:
			date = datetime.datetime.now().strftime('%Y%m%d%H')

			# 遍历waiting_transfer目录，如果非空则代表有文件需要传送，否则continue
			filelist = os.listdir(from_path)
			if len(filelist) > 0 :
				# 去除文件扩展名
				# name_without_ext = os.path.splitext(filelist[0])[0]
	
				if date[8:] in ('13','23'):	
					#print 'Begin to transfer'
					# 将文件传送到远端的WAIT_UPDATE_PATH目录，当远端更新数据库之前会将文件复制一份到BACKUP_PATH目录做为备份
					child = pexpect.spawn('scp %s/%s root@%s:%s/%s' % (from_path,filelist[0],remote_addr,to_path,filelist[0]))
					returncode = child.expect('%s@%s\'s password:' % (remote_user,remote_addr))
					if returncode == 0:
						child.sendline(remote_pwd)
						child.expect(pexpect.EOF)
						#print 'Transfer finished'
						# 传送完成，清空待传送目录
						subprocess.check_call('rm -f %s' % from_path + '/*',shell=True)
					else:
						pass
				else:
					pass
			else:
				pass
		except Exception,e:
			print e
			loger.exception(e)
		time.sleep(60);

if __name__ == '__main__':
	FORMAT = '%(asctime)s - %(levelname)s - %(module)s : %(message)s'
	logging.basicConfig(filename='db_transfer.log',format=FORMAT)
	loger = logging.getLogger('root')	
	# args: from_path,to_path,remote_user,remote_pwd,remote_addr
	# 将会同的数据库备份文件传输到平台保存
	threading.Thread(target=transfer_dmp,args=(CENTER_TRANS_PATH,CENTER_BACKUP_PATH,HT_USER,HT_PWD,HT_ADDRESS,loger)).start()
