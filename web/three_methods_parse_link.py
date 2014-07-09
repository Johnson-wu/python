#coding:utf-8

from HTMLParser import HTMLParser
from cStringIO import StringIO 
from urllib2 import urlopen
from urlparse import urljoin

from BeautifulSoup import BeautifulSoup, SoupStrainer
from html5lib import parse, treebuilders

URLs = {
	'http://python.org',
	'http://goolge.com'
}

def output(x):
	print '\n'.join(sorted(set(x)))

# BeautifulSoup
def simpleBS(url, f):
	output(urljoin(url, x['href']) for x in BeautifulSoup(f).findAll('a'))

# BeautifulSoup : only parse anchor
def fasterBS(url, f):
	output(urljoin(url, x['href']) for x in BeautifulSoup(f, parseOnlyThese=SoupStrainer('a')))

# HTMLParser
def htmlparser(url, f):
	class AnchorParser(HTMLParser):
		def handle_starttag(self, tag, attrs):
			if tag != 'a':
				return 
			if not hasattr(self, 'data'):
				self.data = []
			for attr in attrs:
				if attr[0] == 'href':
					self.data.append(attr[1])

	parser = AnchorParser()
	parser.feed(f.read())
	output(urljoin(url, x) for x in parser.data)

# html5lib : only parse anchor
def html5libparse(url, f):
	# 没有simpletree这个属性
	# output(urljoin(url, x.attributes['href']) \
	# 	for x in parse(f, treebuilder='etree') if isinstance(x, treebuilders.etree.Element) and \
	# 	x.name == 'a')
	for x in parse(f):
		# print type(x)
		print x.tag

def process(url, data):
	# print '\n*** simple BS BeautifulSoup'
	# simpleBS(url, data)
	# data.seek(0)
	# print '\n*** faster BS BeautifulSoup'
	# fasterBS(url, data)
	# data.seek(0)
	# print '\n*** HTMLParser'
	# htmlparser(url, data)
	# data.seek(0)
	print '\n*** HTML5lib'
	html5libparse(url, data)

def _main():
	for url in URLs:
		f = urlopen(url)
		# StringIO — Read and write strings as files
		# When a StringIO object is created, it can be initialized to an existing string by passing the string to the constructor. 
		# If no string is given, the StringIO will start empty. In both cases, the initial file position starts at zero.
		data = StringIO(f.read())
		f.close()
		process(url, data)



if __name__ == '__main__':
	_main()