#coding:utf-8

from socket import *
import time

HOST = '127.0.0.1'
PORT = 22222
BUFFSIZE = 1024
ADDR = (HOST, PORT)

udpCliSoc = socket(AF_INET, SOCK_DGRAM)
# udpCliSoc.bind(ADDR)
udpCliSoc.settimeout(3)		

while True:
	try:
		data = raw_input('>>>')
		if not data:
			break
		udpCliSoc.sendto(data, ADDR)
		data, address = udpCliSoc.recvfrom(BUFFSIZE)
		if not data:
			break
		print data
	except Exception, e:
		print e
		continue
udpCliSoc.close()