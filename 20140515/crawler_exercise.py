from crawler import Crawler
from bs4 import BeautifulSoup
import urllib.parse
import urllib.request
import json

class MyCrawler(Crawler):
	
	def process_document(self, doc, file):
		if doc.status == 200:
			# print('[%d] %s' % (doc.status, doc.url))
			file.write(doc.url+'\n')
			try:
				soup = BeautifulSoup(doc.text.decode('gb18030').encode('utf-8'))
			except Exception as e:
				print(e)
				soup = BeautifulSoup(doc.text)
			# print(soup.find(id="product-intro").div.h1.text)
			file.write(soup.find(id="product-intro").div.h1.text+'\n')
			
			url_id = urllib.parse.unquote(doc.url).split('/')[-1].split('.')[0]
			
			# 这个网址是如何得来的？
			f = urllib.request.urlopen('http://p.3.cn/prices/get?skuid=J_'+url_id,timeout=5)
			
			# info = f.info()
			# print("Info: ",info)
			str = f.read()
			# f.read() 返回的是bytes型，需要转换为string
			# json.loads() ？？？
			price = json.loads(bytes.decode(str))
			f.close()
			# print(price[0]['p'])
			# json.dumps() 可以将list，转换为str ？？？			
			file.write(json.dumps(price)+'\n\n\n')
		else:
			pass

crawler = MyCrawler()
crawler.set_follow_mode(Crawler.F_SAME_HOST)
crawler.set_concurrency_level(16)
crawler.add_url_filter('\.(jpg|jpeg|gif|png|js|css|swf)$')
crawler.crawl('http://item.jd.com/574503.html')
			