#coding:utf-8
# import http.client as client

# file_content = open('test.txt').read()
# conn = client.HTTPConnection('localhost',9999)
# conn.request('PUT','/file',file_content)
# response = conn.getresponse()
# print(response.status,'---', response.reason)

import socket

f = open('test1.txt','a')
HOST = 'localhost'
PORT = 9999
soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
soc.connect((HOST,PORT))
while True:
	data = soc.recv(1024)
	print('client',str(data))
	print(not data)
	if not data:
		break
	else:
		f.write(str(data))
f.close()