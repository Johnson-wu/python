#coding:utf-8

import socket
import time

HOST, PORT = 'localhost', 10001

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def recvfile(filename):
	print('Client: start recieve file...')
	f = open('client_receive.txt','wb')
	while True:
		data = socket.recv(4069)
		print(data)
		if data == bytes('EOF','utf-8'):
			print('Client : I\'ve successfully received file')
			break
		f.write(data)
	f.close()
	socket.sendall(bytes('EOF','utf-8'))


def sendfile(filename):
	print('Client: start transfer file...')
	f = open(filename, 'rb')	# b 代表以binary的模式操作文件
	while True:
		data = f.read(4069)
		if not data:
			# 放在这里的话，服务端接收时会有问题，EOF和文件内容一起接收了。
			# 这样的话，服务端匹配不到“EOF”,就会一直等待下去
			# socket.sendall(bytes('EOF','utf-8'))	
			break
		print('sending ',data)
		socket.sendall(data)
	f.close()
	time.sleep(1)
	socket.sendall(bytes('EOF','utf-8'))
	data = socket.recv(4069)
	if data == bytes('EOF','utf-8'):
		print('Client : sever have recieved file successfully')

def confirm_with_server(socket, cmd):
	socket.send(bytes(cmd,'utf-8'))
	data = socket.recv(4069)
	# print('client get comfirm data is : ',data)
	if str(data,'utf-8') == 'ready':
		return True
	else:
		return False


# 为什么连接只能用一次？再次input时就断开了？
try:
	socket.connect((HOST,PORT))
	while True:
		argv = input('请输入指令(格式为:command filepath) >>>')
		cmd, filename = argv.split()
		if not argv:
			print('指令错误，请正确输入指令！')
			continue

		if confirm_with_server(socket, cmd):
			if cmd == 'put':
				sendfile(filename)
			elif cmd == 'get':
				recvfile(filename)
			elif cmd == 'end':
				socket.close()
			else:
				print('未知指令，请联系系统管理员！')
				continue
		else:
			print('与服务器协议失败！请联系系统管理员！')
except Exception as e:
	raise e
finally:
	# socket.close()
	pass
