#coding:utf-8

import psycopg2 as postgres

CONNECT_PARAM_01 = 'dbname=openerp user=postgres password=root'
CONNECT_PARAM_02 = 'dbname=test user=postgres password=root'
DELIMETER = '===================================================='

def get_conn(param):
	try:
		conn = postgres.connect(param)
		return conn
	except Exception as e:
		print('Failed to connect! Exception:', e)
		return None
	
def get_cursor(conn):
	try:
		cur = conn.cursor()
		return cur
	except Exception as e:
		print('Failed to get cursor! Exception:', e)
		return None

def create_table(cur, sql):
	try:
		cur.execute(sql)
	except Exception as e:
		print('Failed to create table! Exception:', e)

def insert_table(cur, sql):
	try:
		cur.execute(sql)
	except Exception as e:
		print('Failed to insert table! Exception:', e)

def exec_select(cur, tablename, *args):
	try:
		if len(args) > 0:
			sql = len(args) == 1 and args[0] or ','.join(args)	# python中的三元表达式和java中格式不同: condition and result1 or result2
			# sql = ','.join(args)	# 将参数用','连接
			sql = 'select ' + sql + ' from ' + tablename
			# print(sql)
			cur.execute(sql)
		else:
			cur.execute('select * from %s' % tablename)
		# return cur
	except Exception as e:
		print('Failed to select! Exception:', e)
		# return None
	
def release_resources(*args):
	for arg in args:
		arg.close()


def print_all_selected(cur):
	while True:
		data = cur.fetchone()
		if data:
			print(data)
		else:
			print(DELIMETER)
			break



if __name__ == '__main__':
	# conn = get_conn(CONNECT_PARAM_01)
	# cur = get_cursor(conn)
	# exec_select(cur,'project_task_work','id','name','x_note','x_problem')
	# print_all_selected(cur)
	
	# exec_select(cur,'project_task_work','*') 
	# print_all_selected(cur)

	# exec_select(cur,'project_task_work','name') 
	# print_all_selected(cur)

	# release_resources(cur, conn)

	conn = get_conn(CONNECT_PARAM_02)
	cur = get_cursor(conn)

	sql = 'CREATE TABLE test01 (id serial PRIMARY KEY, num integer, data varchar);'
	create_table(cur,sql)
	sql = "INSERT INTO test01 (num, data) VALUES(100,'abc');"
	insert_table(cur,sql)
	exec_select(cur,'test01')
	print_all_selected(cur)
	release_resources(cur, conn)

	
		


