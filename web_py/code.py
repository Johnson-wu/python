#coding:utf-8

import web
import blog

urls = (
	'/blog',blog.app_blog,
	'/(.*)','index'
)

class index():
	def GET(self, path):
		return 'index ' + path


if __name__ == '__main__':
	app = web.application(urls, locals())
	app.run()

