#coding:utf-8

import web

urls = ('/hello','index')

class index:
	def GET(self):
		return 'Hello pythoner ! I am web.py .'


if __name__ == '__main__':
	app = web.application(urls, globals())
	app.run()