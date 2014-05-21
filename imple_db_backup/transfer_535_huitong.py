#coding:utf-8

import subprocess,threading
import pexpect
import datetime,os,time as timer

PATH = '/home/why/db_transfer_535_huitong'
HAS_TRANSFER = False
IDENTIFIER = '535'

def transfer_dmp():
	localfilename = PATH + '/' + now[0] + '.dmp'
	remotefilename = PATH + '/' + now[0] + '-huitong.dmp'

	while True:
		now = datetime.datetime.now()
		now = str(now).split()
		date = now[0].split('-')
		time = now[1].split(':')
		# print 'localfilename:%s \\\nremotefilename:%s' % (localfilename,remotefilename)
		
		if time[0] == '01':
			HAS_TRANSFER = False
		
		if len(os.listdir(PATH)) > 1 and date[2] == '21' and time[0] == '13':
			subprocess.call('rm -f *-*-1*.dmp',shell=True)
			
		if not HAS_TRANSFER and time[0] == '23':	
			child = pexpect.spawn('scp /home/why/db_backup/%s root@27.136.230.5:/home/why/db_backup/%s' % (localfile,remotefile))
			returncode = child.expect('root@27.136.230.5\'s password:')
			if returncode == 0:
				child.sendline('123456')
				child.expect(pexpect.EOF)
				HAS_TRANSFER = True;
			else:
				continue
		timer.sleep(60);

threading.Thread(target=transfer_dmp,args=()).start()
