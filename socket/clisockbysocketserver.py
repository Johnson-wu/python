#coding:utf-8

from socket import *
import time

HOST = '127.0.0.1'
PORT = 22225
BUFFSIZE = 1024
# tcpCliSoc = socket(AF_INET, SOCK_STREAM)
# tcpCliSoc.settimeout(2)
# tcpCliSoc.connect((HOST,PORT))


while True:
	try:	
		tcpCliSoc = socket(AF_INET, SOCK_STREAM)
		tcpCliSoc.settimeout(2)
		tcpCliSoc.connect((HOST,PORT))
		data = raw_input('>>>')
		if not data:
			break
		result = tcpCliSoc.send(data + '\n')
		# print result
		while True:
			data = tcpCliSoc.recv(BUFFSIZE)
			if not data:
				break
			print data
	except Exception, e:
		print e
		continue
tcpCliSoc.close()