#coding:utf-8

# MIMEImage, MIMEMultipart, MIMEText are both subclass of Message
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from smtplib import SMTP_SSL

HOST = 'smtp.qq.com'
SENDER = 'wu_yi_fan2013@qq.com'
USER = 'wu_yi_fan2013'
PWD = '830824wujing'
RECIPS = ['wujingjingjing@163.com','wu_yi_fan2013@163.com']

# multipart alternative : text and html
def make_mpa_msg():
	# class email.mime.multipart.MIMEMultipart([_subtype[, boundary[, _subparts[, _params]]]]) 
	# 		_subparts is a sequence of initial subparts for the payload. 
	# 			It must be possible to convert this sequence to a list.
	# 			You can always attach new subparts to the message by using the Message.attach() method.
	email = MIMEMultipart('alternative')	# ???
	text = MIMEText('Hello World!\r\n','plain')
	email.attach(text)
	html = MIMEText(
			'<html><body><h4>Hello World! Html</h4></body></html>', 'html'
		)
	email.attach(html)
	return email	# email is also a Message object

#mutipart : images
def make_img_msg(fn):
	f = open(fn, 'r')
	data = f.read()
	# f.close()
	email = MIMEImage(data, name=fn)
	# ???
	email.add_header('Content-ID',
		'',filename=fn)
	return email

def sendMsg(fr, to, msg):
	s = SMTP_SSL(HOST)
	s.login(USER,PWD)
	err = s.sendmail(fr, to , msg)
	s.quit()

if __name__ == '__main__':
	print 'Sending multipart alternative msg ...'
	msg = make_mpa_msg()
	msg['From'] = SENDER
	msg['To'] = ','.join(RECIPS)
	msg['Subject'] = 'multipart alternative test'
	# msg.as_string() ???
	sendMsg(SENDER, RECIPS, msg.as_string())

	# 为什么图片发送成功，但是图像花了？？？
	print 'Sending multipart image ...'
	msg = make_img_msg('E:\\GitHub\\python\\e-mail\\1.jpg')
	msg['From'] = SENDER
	msg['To'] = ','.join(RECIPS)
	msg['Subject'] = 'multipart image test'
	sendMsg(SENDER, RECIPS, msg.as_string())
