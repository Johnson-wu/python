#coding:utf-8
# 这个例子可以很清楚验证semaphore

import threading
import time
from atexit import register

sema = threading.Semaphore(2)

def test():
	print 'request to acquire semaphore...'
	sema.acquire()
	print '%s acquire a semaphore' % threading.current_thread()
	time.sleep(2)
	print '%s release a semaphore' % threading.current_thread()
	sema.release()


def _main():
	for i in range(5):
		threading.Thread(target=test,args=()).start()

@register
def _atexit():
	print 'All subthread done...'


if __name__ == '__main__':
	_main()

