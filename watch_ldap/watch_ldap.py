#coding:utf-8

import subprocess,time

def start_watch(procname, role):
	while True:
		try:
			ps = subprocess.Popen('ps -ef|grep %s' % role, shell=True, stdout=subprocess.PIPE)
			result = ps.stdout.read()
			if procname in result:
				# print 'continue'
				pass
			else:
				# print 'restart'
				subprocess.call('sh /home/huitong/restart_apachds.sh', shell=True)
		except Exception, e:
			print e
			continue
		finally:
			time.sleep(180)


start_watch('/opt/apacheds', 'apacheds')
