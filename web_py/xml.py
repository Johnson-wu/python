#coding:utf-8

import web

render =  web.template.render('templates', cache=False)

urls = ('/(.*)','index')

class index():
	def GET(self, code):
		web.header('Content-Type','text/xml')
		print render.test(code)
		return render.response(code)	# render.XXX() 中XXX代表的是template的文件名称，如果templates文件夹下没有名为response的文件会报错
		# return render.test(code)

def my_processor(handler):
	print 'before handling'
	# 这个handler()应该是在app.add_processor()时，web.py自动生成并传入的，作用是用来handle request
	result = handler()
	print 'after handler\n'
	return result

# web.py 本身提供调试的工具
web.webapi.internalerror = web.debugerror
if __name__ == '__main__':
	app = web.application(urls, globals())
	app.add_processor(my_processor)
	
	app.run()





