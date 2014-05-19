#coding:utf-8
# threading练习：threading 模块是对_thread模块的二块封装，提供了更方便的API来操作线程。
# 有两种方法可以创建线程，一种是继承，一种是创建threading.Thread对象，并传入相应的参数

import threading,time

count = 0

class MyThread(threading.Thread):
	def __init__(self, lock, threadname):
		super(MyThread,self).__init__(name=threadname)
		self.lock = lock

	def run(self):
		global count
		# 加不加锁没有什么区别，java中还会出现交叉打印的现象，在python中目前还没有遇见
		for i in range(10):
			count += 1
		print('%s : %d' % (self.name,count))

lock = threading.Lock

for i in range(5):
	MyThread(lock, 'thread-%d' % i).start()

