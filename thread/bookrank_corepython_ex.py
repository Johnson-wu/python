#coding:utf-8

from atexit import register
from re import compile
from threading import Thread 
from time import ctime
from urllib2 import urlopen as uopen 

REGEX = compile('#([\d,]+) in Books')
AMZN = 'http://amazon.com/dp/'
ISBNs = {
	'0132269937': 'Core Python Programming',
	'0132356139': 'Python Web Development with Django',
	'0137143419': 'Python Fundamentals',
}

# 这里返回的应该是该书在amazon上的销量排行榜上的排名
def getRanking(isbn):
	page = uopen('%s%s' % (AMZN, isbn))
	data = page.read()
	page.close()
	return REGEX.findall(data)[0]

def _showRanking(isbn):
	print '- %r ranked %s' % (ISBNs[isbn],getRanking(isbn))

def _main():
	print 'At', ctime(), 'on Amazon...'
	for isbn in ISBNs:
		# _showRanking(isbn)
		Thread(target=_showRanking,args=(isbn,)).start()

# atexit.register(func[, *args[, **kargs]]) 
# 		Register func as a function to be executed at termination. Any optional arguments that are to be passed to func must be passed 
# 		as arguments to register(). It is possible to register the same function and arguments more than once.
# 		At normal program termination (for instance, if sys.exit() is called or the main module’s execution completes),
# 		all functions registered are called in last in, first out order. The assumption is that lower level modules will normally 
#		 be imported before higher level modules and thus must be cleaned up later.
# 		If an exception is raised during execution of the exit handlers, a traceback is printed (unless SystemExit is raised) and 
# 		the exception information is saved. After all exit handlers have had a chance to run the last exception to be raised is re-raised.
@register
def _atexit():
	print 'all Done at:',ctime()

if __name__ == '__main__':
	_main()