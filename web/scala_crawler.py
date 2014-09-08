#coding:utf-8

import cStringIO
import formatter
from htmllib import HTMLParser
import httplib
import os
import sys
import urllib
import urlparse

class MyHTMLParser(HTMLParser):
	def __init__(self,url):
		self.url = url
		self.already_download = []
		self.need_download = []

	# 递归解析传入的url，分析出所有符合要求的href地址，下载并加入already_download列表 
	def parse_links(self,pattern):
		pass
		return list

	# 解析url在本地文件系统中创建相应的目录
	def get_file(self, url, default='index.html'):
		parsed = urlparse.urlparse(url)
		print parsed
		print parsed.netloc
		print parsed.netloc.split('@')
		# print parsed.netloc.split('@')[-1]
		# print parsed.netloc.split('@')[-1].split(':')
		host = parsed.netloc.split('@')[-1].split(':')[0]
		# print host
		filepath = '%s%s' % (host, parsed.path)

		if not os.path.splitext(parsed.path)[1]:
			filepath = os.path.join(filepath, default)
		linkdir = os.path.dirname(filepath)
		print filepath, linkdir
		if not os.path.isdir(linkdir):
			# Recursive directory creation function. 
			# Like mkdir(), but makes all intermediate-level directories needed to contain the leaf directory.
			# 对于相对路径，会在当前目录下递归创建目录
			os.makedirs(linkdir)
		return filepath

	def download(self,url,f):
		try:
			# urllib.urlretrieve(url[, filename[, reporthook[, data]]]) 
			# 		Copy a network object denoted by a URL to a local file, if necessary.
			# 		If the URL points to a local file, or a valid cached copy of the object exists, the object is not copied.
			# 		Return a tuple (filename, headers) where filename is the local file name under which the object can be found, 
			# 		and headers is whatever the info() method of the object returned by urlopen() returned (for a remote object, possibly cached). 
			retval = urllib.urlretrieve(url, f)
		except Exception, e:
			retval = (('*** Error: bad URL "%s": %s' % (self.url, e)),)
		# print 'retval: ', retval
		return retval



def _main():
	url = 'http://www.artima.com/pins1ed/index.html#TOC'
	parser = MyHTMLParser(url)
	f = parser.get_file(url)
	res = parser.download(url,f)
	print res

if __name__ == '__main__':
	_main()