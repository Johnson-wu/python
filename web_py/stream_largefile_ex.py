#coding:utf-8

# Simple streaming server demonstration
# Uses time.sleep to emulate a large file read
# 这个例子只是用time.sleep模拟browser边接收服务端的数据，边display

import web
import time

urls = (
	'/','count_holder',
	'/(.*)','count_down'
)

app = web.application(urls, globals())

class count_down:
	def GET(self, count):
		web.header('Content-Type','text/html')
		# this header will tell browser how to display data.
		# If not , the browser will buffer all data before displaying it to you
		web.header('Transfer-Encoding','chunked')
		yield '<h2>Prepare for Lanch!</h2>'
		yield '<ul>'
		count = int(count)
		j = '<li>Lift off in %s...</li>'
		for i in range(count,0,-1):
			out = j % i
			time.sleep(1)
			yield out
		yield '</ul>'
		time.sleep(1)
		yield '<h1>Lift off</h1>'


class count_holder:
	def GET(self):
		web.header('Content-Type','text/html')
		web.header('Transfer-Encoding','chunked')
		boxes = 4
		delay = 3
		countdown = 10
		for i in range(boxes):
			# iframe 中的 src 指向了内嵌视窗所要显示页面的地址，在本例就是'/count',调用count_down
			output = '<iframe src="/%d" width="200" height="500"></iframe>' % (countdown - i)
			yield output
			time.sleep(delay)


if __name__ == '__main__':
	app.run()