#coding:utf-8

import threading
from time import ctime, sleep

loops = (4,2)

# 自定义线程，但是要重写__init__及run()方法
class MyThread(threading.Thread):

	def __init__(self, func, args, name=''):
		threading.Thread.__init__(self)
		self.func = func
		self.args = args
		self.name = name

	def run(self):
		print '%s func start at %s' % (self.name, ctime())
		self.result = self.func(*self.args)
		print '%s func end at %s' % (self.name, ctime())

	def getResult(self):
		return self.result


def loop(index, nsec):
	print 'start loop', index, 'at:', ctime()
	sleep(nsec)
	print 'loop', index, 'done at:', ctime()

def main():
	print 'starting at:', ctime()
	threads = []
	nloops = range(len(loops))

	for i in nloops:
		t = MyThread(loop, (i, loops[i]), loop.__name__)
		threads.append(t)

	for i in nloops:
		threads[i].start()

	for i in nloops:
		# use join() , the main thread will wait untill this thread exit
		threads[i].join()

	print 'All Done at :', ctime()


if __name__ == '__main__':
	main()