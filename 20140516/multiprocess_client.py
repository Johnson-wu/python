# -*- coding:utf-8 -*-

__author__ = 'Johnson'
__license__ = 'Johnson@2014-05-16'

from multiprocessing.connection import Client

a = 0 
try:
	while True:
		a += 1
		address = ('localhost', 8888)
		# conn = Client(address, authkey=bytes('johnson wu', 'utf-8')) # Client()是multiprocessing.connection的一个function
		conn = Client(address)
		b = conn.recv()
		# print('a:%d---b:%s' % (a,b))
		conn.close()
except Exception as e:
	raise e

  

