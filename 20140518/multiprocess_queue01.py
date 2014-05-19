#coding:utf-8
# Queue 和pipe一样也遵行先进先出的规则，允许多进程存和取的操作（前面pipe测试时也支持多进程！）
# 感觉queue 比 pipe要好用一些，至少在下面测试打印输出时，顺序不会让我迷惑

import os,time
import multiprocessing as multiproc

def inputQ(queue):
	print('Process %s input a message !' % os.getpid())
	queue.put([('Process %s input a message !' % os.getpid()), multiproc.current_process().pid])

def outputQ(queue):
	print('Process %s get the message : \n %s' % (os.getpid(),queue.get()))


if __name__ == '__main__':
	queue = multiproc.Queue()
	in_process_list = []
	out_process_list = []

	for i in range(5):
		process = multiproc.Process(target=inputQ,args=(queue,))
		in_process_list.append(process)
		process.start()

	for i in range(5):
		process = multiproc.Process(target=outputQ,args=(queue,))
		out_process_list.append(process)
		process.start()

	time.sleep(2)

	for process in in_process_list:
		process.join()

	queue.close()

	for process in out_process_list:
		process.join()