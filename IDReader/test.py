#coding:utf-8

from ctypes import *
import threading
import time

PATH = 'E:\\IDReader\\'

def getIDInfos():
	while True:	
		# por_res = std.InitComm(c_int(1001))
		auth_res = std.Authenticate()

		if auth_res == 1:
			name = 'a'*32
			gender = 'b'*4
			folk = 'c'*11
			birthday = 'd'*10
			code = 'e'*20
			addr = 'f'*72
			agency = 'g'*32
			expireStart = 'h'*10
			expireEnd = 'i'*10

			p_name = c_char_p(name)
			p_gender = c_char_p(gender)
			p_folk = c_char_p(folk)
			p_birthday = c_char_p(birthday)
			p_code = c_char_p(code)
			p_addr = c_char_p(addr)
			p_agency = c_char_p(agency)
			p_expireStart = c_char_p(expireStart)
			p_expireEnd = c_char_p(expireEnd)

			result = std.ReadBaseInfos(p_name,p_gender,p_folk,p_birthday,p_code,p_addr,p_agency,p_expireStart,p_expireEnd)

			if result == 1:
				print 'name:%s---gender:%s---folk:%s---birthday:%s---code:%s---addr:%s---agency:%s---expireStart:%s---expireEnd:%s '\
						 % (p_name.value.decode('gbk').encode('utf-8').strip(),p_gender.value.decode('gbk').encode('utf-8'),p_folk.value.decode('gbk').encode('utf-8'),\
						 	p_birthday,p_code,p_addr.value.decode('gbk').encode('utf-8'),p_agency.value.decode('gbk').encode('utf-8'),p_expireStart,p_expireEnd) 
		time.sleep(0.5)


if __name__ == '__main__':
	std = windll.LoadLibrary('sdtapi.dll')
	res = std.InitComm(c_int(1001))
	if res == 1:
		print 'I\'m ready...'
		threading.Thread(target=getIDInfos, args=()).start()
		# print 'Close : ',std.CloseComm()
	else:
		print 'Please check device...'
	