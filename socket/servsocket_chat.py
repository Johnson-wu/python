#coding:utf-8

from socket import *
import time
import threading

HOST = ''
PORT = 33331
ADDR = (HOST, PORT)
BUFFSIZE = 1024
IDENT = 'From Server : '

def recv_message(soc, buff):
	while True:
		data = soc.recv(buff)
		if not data:
			continue
		print data

def send_message(soc, identifier, buff):
	while True:
		data = raw_input('>>>')
		if not data:
			continue
		soc.send(identifier + data)


if __name__ == '__main__':
	tcpServSoc = socket(AF_INET, SOCK_STREAM)
	tcpServSoc.bind(ADDR)
	tcpServSoc.listen(10)
	while True:
		tcpCliSoc, addr = tcpServSoc.accept()
		threading.Thread(target=recv_message, args=(tcpCliSoc,BUFFSIZE)).start()
		threading.Thread(target=send_message, args=(tcpCliSoc,IDENT,BUFFSIZE)).start()


