#coding:utf-8

import socketserver
import subprocess
import time

# 定义自己的handler,每当server端接受到一个client请求，就会新建一个handler
class MyTcpHandler(socketserver.BaseRequestHandler):

	def test01(self):
		self.data = self.request.recv(1024).strip()
		print(self.data)
		slef.request.sendall(self.data.upper())

	# 自定义的handler，需要重写handle()方法，用来处理请求
	def handle(self):
		# 为什么调用不了test01()，报NameError: global name 'test01' is not defined
		# test01() 
		self.data = self.request.recv(1024).strip()
		print(self.data)
		self.request.sendall(self.data.upper())



if __name__ == '__main__':
	HOST, PORT = 'localhost', 10000
	server = socketserver.TCPServer((HOST, PORT), MyTcpHandler)

	# Activate server and the server will run forerver util be teminated .
	server.serve_forever()