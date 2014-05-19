# coding:utf-8
# 第二种方式创建线程

import threading

count = 0

def add():
	global count
	for i in range(10):
		count += 1
	print('%s : %d ' % (threading.current_thread().name,count))

lock = threading.Lock 

for i in range(5):
	# 通过创建一个Thread对象，将该线程要调用的对象当作参数传入
	threading.Thread(target=add,args=(),name=('thread-'+str(i))).start()

print(count)