#coding:utf-8

import web

# web.ctx 是一个字典结构，保存每个HTTP请求的特定信息，比如客户端环境变量。可以从中获取很多有用信息

urls = (
	'/(.*)','example'
)

class example:
	# GET(self,path) 中的path，对应于urls中的请求路径，如果urls为上面有请求路径，则这时若get少了path参数，会报参数数量错误
	# path还是应该加上
	def GET(self,path):
		# HTTP_REFERER 获取用户是从哪个网页跳转过来，如果没有，则返回第二个参数
		referer = web.ctx.env.get('HTTP_REFERER','http://www.baidu.com')
		print web.ctx.home
		print web.ctx.method
		print web.ctx.protocol
		print web.ctx.path   # 获取当前请求路径
		# 重定向到referer
		raise web.seeother(referer)	


if __name__ == '__main__':
	app = web.application(urls, globals())
	app.run()
