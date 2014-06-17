#coding:utf-8

from socket import *
import time

HOST = ''
PORT = 22222
BUFFSIZE = 1024


tcpSerSoc = socket(AF_INET, SOCK_STREAM)
tcpSerSoc.bind((HOST, PORT))
tcpSerSoc.listen(10)	# the maximum clients can be served at the same time

while True:
	try:
		# accept() returns value is a tuple (conn, address), so must use two vars to accept the value. 
		# If only one, etc: tcpCliSoc, tcpCliSoc will be a tuple instead of a socket object.
		tcpCliSoc, addr = tcpSerSoc.accept()
		print 'Server Socket begins to listen clients request......'
		while True:
			data = tcpCliSoc.recv(BUFFSIZE)
			if not data:
				break
			print data
			tcpCliSoc.send('%s--The data returned by Server : %s' % (time.ctime(),data))
		tcpCliSoc.close()
	except Exception, e:
		print e
tcpSerSoc.close()
