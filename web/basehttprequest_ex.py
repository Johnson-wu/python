#coding:utf-8

from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer 

class MyHandler(BaseHTTPRequestHandler):

	def do_GET(self):
		try:
			f = open(self.path[1:],'r')
			print self.path		# 当前脚本所在路径，并不是所有自定义类都有path属性
			self.send_response(200)
			self.send_header('Content-Type','text/html')
			self.end_headers()
			self.wfile.write(f.read())
			f.close()
		except Exception, e:
			self.send_error(404 ,'File %s not found' % self.path)


def _main():
	try:
		server = HTTPServer(('',8888),MyHandler)
		print 'Welcome ! Press Ctrl+C to quit'
		server.serve_forever()
	except KeyboardInterrupt:
		print 'Ctrl+C recieved ! shut down the server...'
		server.socket.close()
	


# class Test(object):
# 	def test(self):
# 		print self.path


if __name__ == '__main__':
	_main()
	# Test().test()
