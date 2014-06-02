#coding:utf-8

import logging
import subprocess as proc
from constant import *

logging.basicConfig(filename='test.log', level=logging.INFO, format = '%(asctime)s - %(levelname)s: %(message)s')
log = logging.getLogger('test')
try:
	# 为什么连接不存在的数据库产生的Exception不能被写进log?
	proc.call('%s/pg_dump -i -h %s -p %s -U %s %s|gzip > %s/%s' % (PGDUMP_CMD_PATH,'1.1.1.114',PORT,DB_USER,'open',BACKUP_PATH,'test.gz'),shell=True)
except Exception as e:
	print(e)
	log.exception(e)
