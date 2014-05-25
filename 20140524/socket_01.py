#coding:utf-8

import socket

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
port = socket.getservbyname('http','tcp')
s.connect(('www.baidu.com',port))

print('Connected from ', s.getsockname())
print('Connected to ', s.getpeername())
print('My machine name ', socket.gethostname())
print('My machine address ', socket.gethostbyname(socket.gethostname()))
print(s.fileno())