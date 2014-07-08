# # -*- coding: utf-8 -*-

# import urllib2

# LOGIN = 'wesley'
# PASSWD = 'you\'llNeverGuess'
# URL = 'http://localhost'
# REALM = 'Secure Archive'

# def handler_version(url):
# 	from urlparse import urlparse
# 	hdlr = urllib2.HTTPBasicAuthHandler()
# 	hdlr.add_password(REALM, urlparse(url)[1], LOGIN, PASSWD)
# 	opener = urllib2.build_opener(hdlr)
# 	urllib2.install_opener(opener)
# 	return url 

# def request_version(url):
# 	from base64 import encodestring
# 	req = urllib2.Request(url)
# 	b64str = encodestring('%s:%s' % (LOGIN, PASSWD))[:-1]
# 	req.add_header('Authorization','Basic %s' % b64str)
# 	return req

# for funcType in ('handler','request'):
# 	print '*** Using %s:' % funcType.upper()
# 	url = eval('%s_version' % funcType)(URL)
# 	print url
# 	f = urllib2.urlopen(url)
# 	print f.readlines()
# 	f.close()


import urllib
from htmllib import HTMLParser
import formatter
import cStringIO

url = 'http://www.163.com'
# page = urllib.urlopen('http://www.163.com')
# date = page.read()
result = urllib.urlretrieve(url, '163.html')
parser = HTMLParser(formatter.AbstractFormatter(formatter.DumbWriter(cStringIO.StringIO())))
# parser.feed('<a href="www.000.com"/><a href="www.001.com"/>')
data = open(result[0],'r').read()
parser.feed(data)
parser.close()
parser.anchorlist
