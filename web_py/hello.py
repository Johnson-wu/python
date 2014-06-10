#coding:utf-8

import web

urls = ('/.*','server')
urls2 = ('/.*/','rediect')

class server():
	def GET(self):
		web.header('Content-Type','text/html')
		return 'Hello client!'


class rediect():
	def GET(self):
		web.seeother('/hello')



if __name__ == '__main__':
	app = web.application(urls,globals())
	response = app.request('/hello')
	print response.data
	print response.headers
	print response.status

	print '======================================'
	app2 = web.application(urls2,globals())
	response2 = app2.request('/hello/',host='127.0.0.1:8080',https=False)
	print response2.data
	print response2.headers
	print response2.status

	print '======================================'
	app.run()	# 启动Web服务器监听，http://localhost:8080/static/1.jpg可以打开服务器上的Static files
	
