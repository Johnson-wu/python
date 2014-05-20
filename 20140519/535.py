#coding:utf-8

# import http.server as server
# port = 9999
# handler = server.SimpleHTTPRequestHandler
# httpd = socketserver.TCPServer(("localhost", port), handler)

# print("serving at port", port)
# httpd.serve_forever()

import socketserver
import codecs

class MyHandler(socketserver.BaseRequestHandler):

	def handle(self):
		f = open('server.txt',encoding='utf-8')
		while True:
			data = f.read(1024)	
			print('server:',str(data))
			if not data:
				break
			else:
				self.request.send(data)
		f.close()


if __name__ == '__main__':
	HOST, PORT = 'localhost', 9999
	server = socketserver.TCPServer((HOST,PORT),MyHandler)
	server.serve_forever()