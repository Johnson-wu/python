#coding:utf-8

from ctypes import *
import threading
import time

PATH = 'E:\\IDReader\\'

def main():
	while True:	
		print std.InitComm(c_int(1001))
		print 'Authenticate : ',std.Authenticate()
		#pMSG = create_string_buffer('\000'*191)
		
		result = std.ReadBaseMsg(pointer(pMSG), pointer(len))
		#std.ReadBaseMsg(byref(pMSG),byref(len))
		print pMSG,'===',result
		time.sleep(1)



if __name__ == '__main__':
	# threading.Thread(target=main, args=()).start()

	std = windll.LoadLibrary(PATH + 'sdtapi.dll')
	prf = windll.msvcrt.printf
	res = std.InitComm(c_int(1001))
	if res == 1:
		print 'I\'m ready...'
		print 'Authenticate : ',std.Authenticate()
		
		# pMSG = c_ubyte(192)
		# length = c_int(192)
		# # result = std.ReadBaseMsg(pointer(pMSG), None)
		# result = std.ReadBaseMsg(pointer(pMSG), pointer(length))
		# print 'pMSG : ',pMSG
		# prf('pMSG : %s\n' % pMSG)

		# name = c_byte(31)
		# gender = c_byte(3)
		# folk = c_byte(10)
		# birthday = c_byte(9)
		# code = c_byte(19)
		# addr = c_byte(71)
		# agency = c_byte(31)
		# expireStart = c_byte(9)
		# expireEnd = c_byte(9)

		# name = c_char_p()
		# gender = c_char_p()
		# folk = c_char_p()
		# birthday = c_char_p()
		# code = c_char_p()
		# addr = c_char_p()
		# agency = c_char_p()
		# expireStart = c_char_p()
		# expireEnd = c_char_p()
		# result = std.ReadBaseInfos(byref(name),byref(gender),byref(folk),byref(birthday),byref(code),byref(addr),byref(agency),byref(expireStart),byref(expireEnd))

		name = 'a'
		gender = 'b'
		folk = 'c'
		birthday = 'd'
		code = 'e'
		addr = 'f'
		agency = 'g'
		expireStart = 'h'
		expireEnd = 'i'
		# result = std.ReadBaseInfos(name,gender,folk,birthday,code,addr,agency,expireStart,expireEnd)

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

		print 'result code : ',result
		# print 'name: ',p_name.value.decode('gbk').encode('utf-8')
		print 'name:%s---gender:%s---folk:%s---birthday:%s---code:%s---addr:%s---agency:%s---expireStart:%s---expireEnd:%s '\
				 % (p_name.value.decode('gbk').encode('utf-8').strip(),p_gender.value.decode('gbk').encode('utf-8'),p_folk.value.decode('gbk').encode('utf-8'),\
				 	p_birthday,p_code,p_addr.value.decode('gbk').encode('utf-8'),p_agency.value.decode('gbk').encode('utf-8'),p_expireStart,p_expireEnd)
		# print 'Close : ',std.CloseComm()
	else:
		print 'Please check device...'
	