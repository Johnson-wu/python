#coding:utf-8

from SocketServer import TCPServer , StreamRequestHandler 
import socket
import time
import os 

HOST = '127.0.0.1'
PORT = 22225

# 使用handler后，一个连接收发一次就被abort了吗？
# StreamRequestHandler 的操作类似于文件操作
class MyRequestHandler(StreamRequestHandler):
	def handle(self):
		print 'Request from %s' % format(self.client_address)
		data = self.rfile.readline()
		print data
		self.wfile.write('%s -- %s' % (time.ctime(), data))
		# socket.getservbyname(servicename) 根据服务名称返回port，直接调用操作系统api.如：http 返回 80
		self.wfile.write('os.name:%s -- directory:%s -- daytime service:%s' % (os.name, os.getcwd(), socket.getservbyname('daytime')))
	

# 为什么接收到请求后，handle没有调起?客户端socket type指定错误sock_dgram
tcpSerSoc = TCPServer((HOST,PORT), MyRequestHandler)
print 'waiting for connection...'
tcpSerSoc.serve_forever()