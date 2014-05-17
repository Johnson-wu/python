# -*- coding:utf-8 -*-
# python中使用线程有两种方式，这里练习第一种方式利用较原始_thread模块来编程，虽然更原始，但是更灵活

# 线程在执行过程中与进程还是有区别的，每个独立的线程有一个程序运行的入口(即进程python *.py)、顺序执行序列和程序的出口，但是线程
# 不能够独立执行，必须依赖在应用程序中，由应用程序提供多个线程执行控制

import _thread, time

count = 0 

def work():
	global count
	for i in range(1000):
		count += 1
		print(count)

for i in range(10):
	# _thread.start_new_thread(function, args[, kwargs]) 
	# 		Start a new thread and return its identifier（标识符）. The thread executes the function function with the argument list 
	# 		args (which must be a tuple). The optional kwargs argument specifies a dictionary of keyword arguments. 
	# 		When the function returns, the thread silently exits. When the function terminates with an unhandled exception, 
	# 		 stack trace is printed and then the thread exits (but other threads continue to run).
	_thread.start_new_thread(work,())  

# 因为主程序和新创建的线程是同时在运行的。如果主程序不等3秒，则主程序会在0.2s就运行结束，那样新建的10个线程没有机会去运行
# ，所以print(count)为0
time.sleep(3)  

print(count)