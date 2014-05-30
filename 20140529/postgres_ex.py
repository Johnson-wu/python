#coding:utf-8

import psycopg2 as postgres

conn = postgres.connect('dbname=openerp user=postgres password=root')

conn.set_client_encoding('utf-8')

cur = conn.cursor()

cur.execute('select id,name,x_note,x_problem from project_task_work')

# cur.fetchone() 每次返回一行数据，数据类型为tuple
while True:
	data = cur.fetchone()
	if data:
		print(data)
	else:
		break

print(cur.fetchone())	# 这时将返回None

conn.commit()

cur.close()

conn.close()