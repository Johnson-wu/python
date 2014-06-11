#coding:utf-8

import web

urls = (
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


if __name__ == '__main__':
	app = web.application(urls, globals())
	app.notfound = notFound
	app.internalerror = internalError
	app.run()