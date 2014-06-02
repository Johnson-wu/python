#coding:utf-8
# 利用锁实现线程间的同步

import threading
import time

class MyThread(threading.Thread):

	def __init__(self, ThreadID, name, counter):
		# 继承时重写__init__方法，必须主动调用父类的__init__方法
		threading.Thread.__init__(self)
		self.ThreadID = ThreadID
		self.name = name
		self.counter = counter

	# 方法有self参数，代表是对象方法，必须实例化后才可以使用
	def run(self):
		print('starting %s' % self.name)
		threadLock.acquire()
		
		print_time(self.name, self.counter, 3)
		threadLock.release()


def print_time(threadName, delay, counter):
	while counter:
		time.sleep(delay)
		# time.ctime([seconds]) 将秒转变为本地时间
		print('%s : %s and counter : %d' % (threadName, time.ctime(time.time()), counter))
		counter -= 1


# 锁也没有传入生成的线程对象中，为什么里面可以直接用了？因为这个练习中是通过实例化对象来生成线程，所以锁的创建还是在实例化线程之前
threadLock = threading.Lock()
threads = []

MyThread_1 = MyThread(1, 'Thread-1', 1)
MyThread_2 = MyThread(2, 'Thread-2', 2)

threads.append(MyThread_1)
threads.append(MyThread_2)

for thread in threads:
	thread.start()

# 等待所有线程完成
for thread in threads:
	thread.join()

print('Exiting main thread')
