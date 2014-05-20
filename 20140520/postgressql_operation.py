#coding:utf-8

import subprocess
import datetime

date = datetime.datetime.now().strftime('%Y-%m-%d')

PGDUMP_CMD_PATH = '/usr/lib/postgresql/9.1/bin'
IP_ADDRESS = 'localhost'
PORT = '5432'
PG_USER = 'postgres'
DB_NAME = 'huitong'
DB_BACKUP_NAME = date + '-huitong.dmp'

subprocess.call('%s/pg_dump -i -h %s -p %s -U %s %s > %s' % (PGDUMP_CMD_PATH,IP_ADDRESS,PORT,PG_USER,DB_NAME,DB_BACKUP_NAME),shell=True)
subprocess.call('%s/dropdb -i -h %s -p %s -U %s %s' % (PGDUMP_CMD_PATH,IP_ADDRESS,PORT,PG_USER,DB_NAME),shell=True)

