#coding:utf-8

import psycopg2
import psycopg2.pool as pool
import time

CONNECT_PARAM = 'dbname=openerp user=postgres password=root host=127.0.0.1'

conn_pool = pool.SimpleConnectionPool(5,5,CONNECT_PARAM)
conn = conn_pool.getconn()
cur = conn.cursor()
sql = 'select id,name,x_note,x_problem from project_task_work'
cur.execute(sql)

while True:
	data = cur.fetchone()
	if data:
		print data
	else:
		break

cur.close()
print 'cur close ...'
time.sleep(3)
conn.close()
print 'conn close ...'
time.sleep(6)
conn_pool.closeall()
print 'pool close ...'


