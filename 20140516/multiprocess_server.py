# -*- coding:utf-8 -*-

from multiprocessing.connection import Listener
from threading import Thread 

# 线程不是比进程更小的单位吗？按照这个程序的演示目的是多进程的通信，怎么为用一个线程去启动多个进程？

def listener():
	address = ('localhost', 8888)
	# 为什么加了authkey就会报出OSError:bad message length ? 超出了最大的长度
	# listener = Listener(address, backlog=100, authkey=bytes('johnson wu', 'utf-8'))
	listener = Listener(address, backlog=100)

	while True:
		conn = listener.accept()
		try:
			print(conn)  # 根据打印出来的conn对象，只是用到了4个进程
			conn.send('hhh')
		except Exception as e:
			raise e
		finally:
			conn.close()
	listener.close()

server_thread = Thread(target=listener)
server_thread.daemon = True
server_thread.start()
server_thread.join(timeout=20)