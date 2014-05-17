# -*- coding:utf-8 -*-

# 多进程与多线程的异同

import os
import threading
import multiprocessing

print('Main: ', os.getpid())

def invoke(sign, lock):
	# 获得lock，同一时间只能有一个线程或进程可以获得lock
	lock.acquire()
	print(sign,' : ', os.getpid())  # os.getpid() 返回的是当前进程的id
	lock.release()
	

record = []
lock = threading.Lock()
for i in range(5):
	thread = threading.Thread(target=invoke, args=('thread', lock))
	thread.start()
	record.append(thread)

# 中止创建的线程
for thread in record:
	thread.join()


# 清空list中的数据，或者直接record = []
del record[:]
lock = multiprocessing.Lock()
for i in range(5):
	if __name__ == '__main__':  # 为什么进程要加这个？？？
		# 怎么感觉这里创建的进程是把当前进程复制了一个！
		process = multiprocessing.Process(target=invoke, args=('Process', lock))
		process.start()
		print(process.pid) # 打出来的结果，让人迷惑！
		record.append(process)

for process in record:
	process.join()




