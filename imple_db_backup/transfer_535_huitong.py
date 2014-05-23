#coding:utf-8

import subprocess,threading
import pexpect
import datetime,os,time as timer
from constant import *

def transfer_dmp():
	while True:
		date = datetime.datetime.now().strftime('%Y%m%d%H')

		# 遍历waiting_transfer目录，如果非空则代表有文件需要传送，否则continue
		filelist = os.listdir(WAIT_TRANS_PATH)
		if len(filelist) > 0 :
			# name_without_ext = os.path.splitext(filelist[0])[0]
	
			if date[8:] == '23':	
				# 将文件传送到远端的WAIT_UPDATE_PATH目录，当远端更新数据库之前会将文件复制一份到BACKUP_PATH目录做为备份
				child = pexpect.spawn('scp %s/%s root@%s:%s/%s' % (WAIT_TRANS_PATH,filelist[0],CENTER_ADDRESS,WAIT_UPDATE_PATH,filelist[0]))
				returncode = child.expect('%s@%s\'s password:' % (CENTER_USER,CENTER_ADDRESS))
				if returncode == 0:
					child.sendline(CENTER_PWD)
					child.expect(pexpect.EOF)
					# 传送完成，清空待传送目录
					subprocess.call('rm -f %s' % WAIT_TRANS_PATH + '/*',shell=True)
				else:
					continue
		else:
			continue
		timer.sleep(60);

threading.Thread(target=transfer_dmp,args=()).start()
