#coding:utf-8

import subprocess
import pexpect
import datetime,os,time as timer

path = '/home/why/db_transfer_535_huitong'
has_transfer = False
while True:
	now = datetime.datetime.now()
	now = str(now).split()
	date = now[0].split('-')
	time = now[1].split(':')
	localfilename = path + '/' + now[0] + '.dmp'
	remotefilename = path + '/' + now[0] + '-huitong.dmp'
	print 'localfilename:%s \\\nremotefilename:%s' % (localfilename,remotefilename)
	
	if time[0] == '01':
		has_transfer = False
	
	if len(os.listdir(path)) > 1 and date[2] == '21' and time[0] == '13':
		child = subprocess.call('rm -f *-*-1*.dmp',shell=True)
		
	if not has_transfer and time[0] == '23':	
		child = pexpect.spawn('scp /home/why/db_backup/%s root@27.136.230.5:/home/why/db_backup/%s' % (localfile,remotefile))
		returncode = child.expect('root@27.136.230.5\'s password:')
		if returncode == 0:
			child.sendline('123456')
			child.expect(pexpect.EOF)
			has_transfer = True;
		else:
			continue
	timer.sleep(60);
