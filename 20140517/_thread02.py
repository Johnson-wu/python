#coding=utf-8

import time, _thread

def work(a, b, c, d, lock):
	lock.acquire()
	print(time.strftime('%H:%M:%S',time.localtime()), '----', a, '----', _thread.get_ident())
	print(time.strftime('%H:%M:%S',time.localtime()), '----', b, '----', _thread.get_ident())
	print(time.strftime('%H:%M:%S',time.localtime()), '----', c, '----', _thread.get_ident())
	print(time.strftime('%H:%M:%S',time.localtime()), '----', d, '----', _thread.get_ident())
	lock.release()


lock = _thread.allocate_lock() # 创建一个全局锁，使得一次只能有一个线程操作work()函数

for x in range(1,5):
	_thread.start_new_thread(work, (1,2,3,4,lock))

time.sleep(5)  # 为什么主线程一定要sleep，创建的线程才会运行？
