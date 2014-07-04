#coding:utf-8

from urllib2 import urlopen

URL = 'http://list.tmall.com/search_shopitem.htm?spm=a220m.1000858.1000725.4.0YvZOp&user_id=1714128138&from=_1_&stype=search&rn=e6da22dca3d554d7cc9406ba76c8707f'

page = urlopen(URL)
data = page.read()
print data.decode('gbk').encode('utf-8')


