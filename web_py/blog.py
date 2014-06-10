#coding:utf-8

import web

urls = (
	'','reblog',
	'/(.*)','blog'
)

# 怎么感觉从code.py过来的请求都会先调用这个类
class reblog():
	def GET(self):
		raise web.seeother('/')	# seeother() 方法？？？


class blog():
	def GET(self, path):
		return 'hello ' + path


app_blog = web.application(urls, locals())
