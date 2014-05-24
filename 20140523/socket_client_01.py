#coding:utf-8

import socket
import sys

HOST, PORT = 'localhost', 10000
# sys.argv 什么作用？是命令运行python脚本时，传递脚本的参数列表
# data = '   '.join(sys.argv[1:])
data = 'Hello world ! Socket ...'

# socket.AF_INET 代表ipv4；socket.SOCK_STREAM 代表socket的类型
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
	socket.connect((HOST,PORT))
	socket.sendall(bytes(data+'\n','utf-8'))
	recieved = str(socket.recv(1024),'utf-8')
except Exception as e:
	raise e
finally:
	socket.close()

print('Send msg : %s ' % data)
print('Recieve msg : %s ' % recieved)