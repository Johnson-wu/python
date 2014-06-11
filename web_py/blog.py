#coding:utf-8

import web

urls = (
	'','reblog',
	'/(.*)','blog'
)

# 怎么感觉从code.py过来的请求都会先调用这个类
# 官方文档里有讲：为了更好的控制大型web应用，web.py支持子程序。在为子程序设计URL模式的时候，
# 				  记住取到的路径(web.ctx.path)是父应用剥离后的。比如，你在主程序定义了URL"/blog"跳转到'blog'子程序，
#				  那没在你blog子程序中所有URL都是以"/"开头的，而不是"/blog"。查看web.ctx取得更多信息。
class reblog():
	def GET(self):
		raise web.seeother('/')	# seeother() 方法？？？


class blog():
	def GET(self, path):
		return 'hello ' + path


app_blog = web.application(urls, locals())
