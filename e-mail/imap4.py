#coding:utf-8

import imaplib

SEND_SERVER = 'smtp.qq.com'
RETR_SERVER = 'imap.qq.com'
USER = 'wu_yi_fan2013'
PWD = '830824wujing'

imap = imaplib.IMAP4_SSL('imap.qq.com')
imap.login(USER,PWD)
direcList = imap.list()
print direcList
rspStatus, msgCount = imap.select()	# 返回应答状态、所选文件夹下的邮件总数(默认为inbox)
print rspStatus, msgCount
rspStatus, data = imap.fetch(msgCount[0],'(BODY[TEXT])') 	# (BODY[TEXT]) 取回的是html中的body中的内容.
print data