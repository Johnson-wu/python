#coding:utf-8
# 很差劲的sample

from atexit import register
from random import randrange
from threading import BoundedSemaphore,Lock,Thread 
from time import ctime,sleep

lock = Lock()
MAX = 5
candytray = BoundedSemaphore(MAX)

def refill():
	lock.acquire()
	print 'Refilling candy ...'
	try:
		candytray.release()
	except Exception, e:
		print 'full, skipping'
	else:
		print 'Refill Successfully !'
	lock.release()

def buy():
	lock.acquire()
	print 'Buying candy ...'
	if candytray.acquire(False):
		print 'You can buy candy...'
	else:
		print 'lack of stock, skipping'
	lock.release()

def producer(loops):
	for i in xrange(loops):
		refill()
		sleep(randrange(3))

def consumer(loops):
	for i in xrange(loops):
		buy()
		sleep(randrange(3))

def _main():
	print 'Starting at :',ctime()
	nloops = randrange(2,6)
	print 'nloops:',nloops
	print 'The Candy Machine (full with %d bars)!' % MAX
	Thread(target=consumer,args=(randrange(nloops,nloops+MAX+2,),)).start()
	Thread(target=producer,args=(nloops,)).start()

@register
def _atexit():
	print 'All Done at : ',ctime()



if __name__ == '__main__':
	print candytray
	_main()