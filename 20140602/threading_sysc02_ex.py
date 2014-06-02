#coding:utf-8
# 利用queue进行线程同步
# 有三种队列：Queue(FIFO), LifoQueue(LIFO), PriorityQueue

import threading
import queue
import time

exitFlag = 0

class MyThread(threading.Thread):
	def __init__(self, threadID, name, q):
		threading.Thread.__init__(self)
		self.threadID = threadID
		self.name = name
		self.q = q

	def run(self):
		print('starting ', self.name)
		process_date(self.name, self.q)
		print('Exiting ', self.name)


def process_date(threadName, q):
	while not exitFlag:
		# 在对队列操作时，先上锁，这样一次只能一个线程对该队列进行操作
		queueLock.acquire()
		if not workQueue.empty():
			# 从队列中取出数据处理，处理完后还可以再放入队列或放入其他队列
			data = q.get()
			queueLock.release()
			print('%s processing %s' % (threadName, data))
		else:
			queueLock.release()
		time.sleep(1)


threadList = ['Thread-1','Thread-2','Thread-3']
nameList = ['One','Two','Three','Four','Five',]

queueLock = threading.Lock()
workQueue = queue.Queue(10)

threads = []
threadID = 1

for name in threadList:
	# 感觉锁也和队列一样做为自定义线程的属性，看上去更明确更易读
	thread = MyThread(threadID, name, workQueue)
	thread.start()
	threads.append(thread)
	threadID += 1

# 填充队列：将需要处理的数据放入队列中，需要时由线程取出
queueLock.acquire()
for name in nameList:
	workQueue.put(name)
queueLock.release()


while not workQueue.empty():
	pass

exitFlag = 1

for thread in threads:
	thread.join()

print('Exiting main thread ')







