#coding:utf-8

# concurrent.futures 是3.2才引入
from concurrent.futures import ThreadPoolExecutor
from re import compile
from time import ctime
from urllib.request import urlopen 

REGEX = compile(b'#([\d,]+) in books')
AMZN = 'http://amazon.com/dp/'
ISBNs = {
	'0132269937': 'Core Python Programming',
	'0132356139': 'Python Web Development with Django',
	'0137143419': 'Python Fundamentals',
}

def getRanking(isbn):
	with urlopen('{0}{1}'.format(AMZN, isbn)) as page:
		return str(REGEX.findall(page.read())[0],'utf-8')

def _main():
	print('At', ctime(), 'on Amazon...')
	with ThreadPoolExecutor(3) as executor:
		for isbn, ranking in zip(ISBNs, executor.map(getRanking, ISBNs)):
			print('- %r ranked %s' % (ISBNs[isbn],ranking))

	print 'all Done at:',ctime()


if __name__ == '__main__':
	_main()