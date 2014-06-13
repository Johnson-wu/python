#coding:utf-8

import web
import wsgilog_ex
import config

urls = (
	'/','example2',
	'/(.*)','example'
)

# 自定义notfound()
def notFound():
	raise web.notfound('Sorry, i can find the page')

# 自定义internalerror()
def internalError():
	raise web.internalerror('Bad request ! internalerror 500')

class example():
	def GET(self,path):
		# raise web.notfound()
		raise web.internalerror()

class example2():
	def GET(self):
		print 'hello'
		raise web.notfound()


if __name__ == '__main__':
	f = file('simple.cfg')
	cfg = config.Config(f)


	app = web.application(urls, globals())
	app.notfound = notFound
	app.internalerror = internalError
	# log = wsgilog_ex.Log(app,cfg)	
	# 如何把cfg传给wsgilog_ex的中件间
	app.run(wsgilog_ex.Log)	 # 会记录所有在控制台的输出到日志文件