#coding:utf-8

import cStringIO
import formatter
from htmllib import HTMLParser
import httplib
import os
import sys
import urllib
import urlparse

class Retriever(object):
	__slots__ = ('url','file')

	def __init__(self, url):
		self.url, self.file = self.get_file(url)

	# 解析url在本地文件系统中创建相应的目录
	def get_file(self, url, default='index.html'):
		parsed = urlparse.urlparse(url)
		host = parsed.netloc.split('@')[-1].split(':')[0]
		# print parsed
		filepath = '%s%s' % (host, parsed.path)

		if not os.path.splitext(parsed.path)[1]:
			filepath = os.path.join(filepath, default)
		linkdir = os.path.dirname(filepath)
		# print filepath, linkdir
		if not os.path.isdir(linkdir):	
			# Remove (delete) the file path. This is the same function as remove(); the unlink() name is its traditional Unix name.
			# os.unlink(linkdir)

			# Recursive directory creation function. 
			# Like mkdir(), but makes all intermediate-level directories needed to contain the leaf directory.
			# 对于相对路径，会在当前目录下递归创建目录
			os.makedirs(linkdir)
		return url, filepath

	# 将下载的url object复制到本地文件中
	def download(self):
		try:
			if os.path.exists(self.file):
				print self.file
				return (self.url, self.file)
			# urllib.urlretrieve(url[, filename[, reporthook[, data]]]) 
			# 		Copy a network object denoted by a URL to a local file, if necessary.
			# 		If the URL points to a local file, or a valid cached copy of the object exists, the object is not copied.
			# 		Return a tuple (filename, headers) where filename is the local file name under which the object can be found, 
			# 		and headers is whatever the info() method of the object returned by urlopen() returned (for a remote object, possibly cached). 
			retval = urllib.urlretrieve(self.url, self.file)
		except Exception, e:
			retval = (('*** Error: bad URL "%s": %s' % (self.url, e)),)
		# print 'retval: ', retval
		return retval

	# 本方法为最核心的方法，用来解析页面
	def parse_links(self):
		f = open(self.file, 'r')
		data = f.read()
		f.close()
		parser = HTMLParser(formatter.AbstractFormatter(formatter.DumbWriter(cStringIO.StringIO())))
		# parser = MyHTMLParser()
		parser.feed(data)
		parser.close()
		# 没有在模块中找到 anchorlist属性
		# 返回页面中所有的锚点，href
		# 该属性在2.6后就被弃用了，如果想用可以通过自定义parser继承HTMLParser来实现，参见evernote.或者用第三方库beautifulsoup
		return parser.anchorlist


class Crawler(object):
	count = 0

	def __init__(self, url, logFile):
		# a queue of links that need to download
		self.q = [url]
		# all links that have been downloaded
		self.seen = set()  # 集合
		parsed = urlparse.urlparse(url)
		# print parsed
		host = parsed.netloc.split('@')[-1].split(':')[0]
		# print host
		self.dom = '.'.join(host.split('.')[-2:])
		# print self.dom
		self.logFile = logFile

	def get_page(self, url, media=False):
		# 先将符合要求的页面下载再进行解析
		r = Retriever(url)
		res = r.download()
		fname = res[0]
		# print "Download result : ",res
		if '***' in fname:
			# print fname, '... skipping parse'
			self.logFile.write('Error : Download Failed --- %s \n' % fname)
			return 

		Crawler.count += 1
		# print '\n(", Crawler.count, ")'
		# print 'URL: ', url 
		# print 'FILE: ', fname
		self.seen.add(url)
		ftype = os.path.splitext(fname)[1]
		# 只下载html文件
		if ftype not in ('.htm','.html'):
			pass
		
		# 对页面中的所有锚点或链接进行分析
		links = r.parse_links()
		for link in links:
			if link.startswith('mailto:'):
				# print '... discarded, mailto link'
				continue
			if not media:
				ftype = os.path.splitext(link)[1]
				if ftype in ('.mp3','.mp4','.m4v','.wav'):
					# print '... discarded, media file'
					continue
			if not link.startswith('http://'):
				link = urlparse.urljoin(url, link)
				# print link

			# print '*', link
			if link not in self.seen:
				if self.dom not in link:
					pass
					# print '... discarded, not in domain'
				else:
					if link not in self.q:
						if 'html' in link or 'htm' in link:
							if 'pins1ed' in link and '#' not in link:
								# 对于页面中符合要求的链接放入self.q列表中
								self.q.append(link)
								# print 'new pins1ed : %s, added to Q---len : %s' % (link,len(self.q))
								self.logFile.write('Url : %s \n === len : %s' % (link,len(self.q)))
						else:
							# self.q.append(link)
							# self.logFile.write('Url : %s \n' % link)
							pass
					else:
						pass
						# print '... discarded, already in Q'
			else:
				pass
				# print '... discarded, already processed'

	def go(self, media=False):
		while self.q:
			url = self.q.pop()
			# print url
			self.get_page(url, media)
		self.logFile.write('Total Download : %s' % Crawler.count)
		self.logFile.close()


class MyHTMLParser(HTMLParser):
    __slots__ = ('url','wait_parse')

    def __init__(self, wait_parse, url):
        HTMLParser.__init__(self)
        self.wait_parse = wait_parse
        self.url = url
 
    def handle_starttag(self, tag, attrs):
        #print "Encountered the beginning of a %s tag" % tag
        if tag == "a":
            if len(attrs) == 0: pass
            else:
                for (variable, value)  in attrs:
                    if variable == "href":
                        if not value.startswith('http://'):
                             value = urlparse.urljoin(url, value)
                             # print value
                        if 'html' in value or 'htm' in value:
                            if 'pins1ed' in value and '#' not in value and value not in wait_parse:
                                self.wait_parse.append(value)
                                # print value
        elif tag == 'img':
            if len(attrs) == 0: pass
            else:
                for (variable, value)  in attrs:
                    if variable == "src":
                        value = urlparse.urljoin(self.url, value)
                        if value not in wait_parse:
                            self.wait_parse.append(value)
        elif tag == 'link':
            if len(attrs) == 0: pass
            else:
                for (variable, value)  in attrs:
                    if variable == "href":
                        value = urlparse.urljoin(self.url, value)
                        if value not in wait_parse:
                            self.wait_parse.append(value) 


def _main():
	# if len(sys.argv) > 1:
	# 	url = sys.argv[1]
	# else:
	# 	try:
	# 		url = raw_input('Enter starting URL: ')
	# 	except Exception, e:
	# 		url = ''
	# if not url:
	# 	return 
	url = 'www.artima.com/pins1ed'
	if not url.startswith('http://') and \
	    not url.startswith('ftp://'):
	    url = 'http://%s/' % url 
	logFile = open(os.path.join(os.getcwd(),'crawler.log'),'a')
	robot = Crawler(url,logFile)
	robot.go()



if __name__ == '__main__':
	_main()

