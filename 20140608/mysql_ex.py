#coding:utf-8
# 练习python mysql操作（尤其是批量操作），日志操作

import MySQLdb as mysql
import logging

# 通过yield来控制方法的进度，每次返回循环中的一对值,类似起到了iterator的作用
def getValue():
	for i in range(3):
		yield(i,'hello'+str(i))

# %(lineno)d 只是调用日志的行号，不是出错的行号，意义不大
FORMAT = '%(asctime)s - %(levelname)s - %(module)s - %(lineno)d : %(message)s'
logging.basicConfig(filename='db.log',format=FORMAT)
loger = logging.getLogger('root')
try:
	conn = mysql.connect('localhost','root','root',port=3306)
	cur = conn.cursor()
	# conn.autocommit(True)
	cur.execute('drop database if exists python')
	cur.execute('create database python')
	conn.select_db('python')
	cur.execute('create table test(id int,info varchar(20))')
	
	# value = [1,'one']
	sql = 'insert into test values(%s,%s)'
	# cur.execute(sql,value)

	# values = [(2,'two'),(3,'three')]
	# values = ((2,'two'),(3,'three'))

	values = getValue()
	cur.executemany(sql,values)

	# getValue()可以返回一个iterater
	print tuple(getValue())

	# 没有commit()，表操作是不会执行的
	conn.commit()
except Exception, e:
	print e
	loger.exception(e)








