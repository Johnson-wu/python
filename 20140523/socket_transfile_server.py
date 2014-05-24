#coding:utf-8

import socketserver
import subprocess
import time

class MyTCPHandler(socketserver.BaseRequestHandler):
	EOF = 'Finished'

	def recvfile(self, filename):
		print('Server : start receiving file...')
		f = open(filename,'wb')
		while True:
			data = self.request.recv(4069)
			if data == bytes('EOF','utf-8'):
				print('Server : I\'ve successful received file')
				break
			print('writing ',data)
			f.write(data)
		f.close()
		self.request.sendall(bytes('EOF','utf-8'))

	def sendfile(self, filename):
		print('Server : start sending file...')
		f = open(filename,'rb')
		while True:
			data = f.read(4069)
			if not data:
				print('Server : i\'ve send the file')
				break
			self.request.sendall(data)
		f.close()
		time.sleep(1)
		self.request.sendall(bytes('EOF','utf-8'))
		data = self.request.recv(4069)
		if data == bytes('EOF','utf-8'):
			print('Sever : client has successfully received')

	def handle(self):
		data = self.request.recv(4069)
		data = str(data,'utf-8')
		print('server get data:',data)
		if data == 'put':
			self.request.sendall(bytes('ready','utf-8'))
			print('Server: ready to receive file...')
			self.recvfile('server_receive.txt')
		elif data == 'get':
			self.request.sendall(bytes('ready','utf-8'))
			print('Server: ready to transfer file...')
			self.sendfile('server_send.txt')


if __name__ == '__main__':
	HOST, PORT = 'localhost', 10001
	server = socketserver.TCPServer((HOST,PORT), MyTCPHandler)
	server.serve_forever()