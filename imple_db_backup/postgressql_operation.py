#coding:utf-8

import subprocess,pexpect
import datetime,time as timer
import re
import threading

date = datetime.datetime.now().strftime('%Y%m%d%H')

PGDUMP_CMD_PATH = '/usr/lib/postgresql/9.1/bin'
IP_ADDRESS = 'localhost'
PORT = '5432'
PG_USER = 'postgres'
DB_NAME = 'huitong'
IDENTIFIER = '535'
DB_BACKUP_NAME = date + '_' + IDENTIFIER + '.dmp'


# 待检！
def kill_process():
	# 首先查看数据库是否被占用，若是则先杀进程，然后再更新数据库
	ps = subprocess.Popen('ps -ef|grep %s' % DB_NAME,shell=True,stdout=subprocess.PIPE)
	ps_result = ps.stdout.read()
	if 'postgres' in ps_result:
		proc_list = re.split(r'postgres.\n',ps_result)
		for proc in proc_list:
			pid = proc.split()[1]
			subprocess.call('kill %s' % pid,shell=True)


# 每天中午1点，晚上23点这两个时段对数据库进行备份。备份的文件名由 日期、所在单位标识 组成
def dump_db():
	while True:
		now = datetime.datetime.now()
		now = str(now).split()
		date = now[0].split('-')
		time = now[1].split(':')

		if time[0] in ('13','23'):
			subprocess.call('%s/pg_dump -i -h %s -p %s -U %s %s > %s' % (PGDUMP_CMD_PATH,IP_ADDRESS,PORT,PG_USER,DB_NAME,DB_BACKUP_NAME),shell=True)


# 待检 ！
# 每天中午1点，晚上23点这两个时段，对数据库进行更新。在更新前检查数据库是否被占用，如果是则杀掉相应进程，然后再更新。
def update_db():
	while True:
		now = datetime.datetime.now()
		now = str(now).split()
		date = now[0].split('-')
		time = now[1].split(':')

		if time[0] in ('13','23'):
			kill_process()
			child = pexpect.spawn('%s/dropdb -i -h %s -p %s -U %s %s' % (PGDUMP_CMD_PATH,IP_ADDRESS,PORT,PG_USER,DB_NAME),shell=True)
			result_code = child.expect('*Are you sure? (y/n)')
			if result_code == 0:
				child.sendline('yes')
				child.expect(pexpect.EOF)
			else:
				continue
			subprocess.call('%s/psql -i -h %s -p %s -U %s %s < %s' % (PGDUMP_CMD_PATH,IP_ADDRESS,PORT,PG_USER,DB_NAME,DB_BACKUP_NAME), shell=True)
		timer.sleep(60)


threading.Thread(target=dump_db,args=()).start()
threading.Thread(target=update_db,args=()).start()