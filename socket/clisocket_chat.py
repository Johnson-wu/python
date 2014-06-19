#coding:utf-8

from socket import *
import time
import threading

HOST = '127.0.0.1'
PORT = 33331
ADDR = (HOST, PORT)
BUFFSIZE = 1024
IDENT = 'From Client : '

def recv_message(soc, buff):
	while True:
		data = soc.recv(buff)
		if not data:
			break
		print data

def send_message(soc, identifier, buff):
	while True:
		data = raw_input('>>>')
		if not data:
			break
		soc.send(identifier + data)


if __name__ == '__main__':
	tcpCliSoc = socket(AF_INET, SOCK_STREAM)
	tcpCliSoc.connect(ADDR)
	threading.Thread(target=recv_message, args=(tcpCliSoc,BUFFSIZE)).start()
	threading.Thread(target=send_message, args=(tcpCliSoc,IDENT,BUFFSIZE)).start()