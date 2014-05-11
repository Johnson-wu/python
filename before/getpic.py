#-*-coding:utf-8-*-
import re
import urllib.request

def getHtml(url):
	req = urllib.request.Request(url)
	response = urllib.request.urlopen(req)
	the_page = response.read()
	return the_page

print(getHtml('http://www.baidu.com'))


