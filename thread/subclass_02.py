#coding:utf-8

import method3_subclass as m3s
from time import ctime,sleep

def fib(n):
	sleep(0.01)
	if n < 2:
		return n
	else:
		return (fib(n-2) + fib(n-1))

def fac(n):
	sleep(0.1)
	if n < 2:
		return n
	else:
		return (n * fac(n-1))

def suma(n):
	sleep(0.1)
	if n < 2:
		return n
	else:
		return (n + suma(n-1))

def main():
	funcs = [fib,fac,suma]
	n = 11
	print 'single thread start at %s' % ctime()
	for elem in funcs:
		print '%s func start at %s' % (elem.__name__, ctime())
		print elem(n)
		print '%s func end at %s' % (elem.__name__, ctime())
	print 'single thread end at %s' % ctime()

	print '==================================\nMulti Thread func start at %s' % ctime()

	threads = []
	for elem in funcs:
		thread = m3s.MyThread(elem, (n,), elem.__name__)
		threads.append(thread)

	for i in range(len(threads)):
		threads[i].start()

	for i in range(len(threads)):
		threads[i].join()

	print 'Multi Thread func end at %s' % ctime()





if __name__ == '__main__':
	main()

