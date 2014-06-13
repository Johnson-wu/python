#coding:utf-8
# 完全不明白，程序也运行不起来
# web.wsgiserver是python的A high-speed, production ready, thread pooled, generic HTTP server.

import web
from web.wsgiserver import CherryPyWSGISever as cherry 

cherry.ssl_certifcate = 'path/to/ssl_certificate'
cherry.ssl_private_key = 'path/to/ssl_private_key'

urls = ('/.*','hello')

class hello:
	def GET(self):
		return 'hello,world'

if __name__ == '__main__':
	app = web.application(urls, globals())
	app.run()