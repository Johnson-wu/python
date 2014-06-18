#coding:utf-8

from socket import *
import time

HOST = ''
PORT = 22222
BUFFSIZE = 1024

udpServSoc = socket(AF_INET, SOCK_DGRAM)
udpServSoc.bind((HOST, PORT))

while True:
	try:
		data, address = udpServSoc.recvfrom(BUFFSIZE)
		udpServSoc.sendto('%s -- %s' % (time.ctime(), data), address)
	except Exception, e:
		print e
udpServSoc.close()