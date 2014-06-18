#coding:utf-8

from socket import *
import time 

HOST = '127.0.0.1'
PORT = 22224
BUFFSIZE = 1024

# Method One : establish a connection
# tcpCliSoc = create_connection((HOST, PORT),10)

# Method Two : establish a connection
tcpCliSoc = socket(AF_INET, SOCK_STREAM)
tcpCliSoc.connect((HOST, PORT))
# tcpCliSoc.setblocking(0)

while True:
	data = raw_input('>>>')
	if not data:
		break
	tcpCliSoc.send('%s--%s' % (time.ctime(),data))
	data = tcpCliSoc.recv(BUFFSIZE)
	print data
tcpCliSoc.close()





