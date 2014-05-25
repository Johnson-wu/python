#coding:utf-8

import smtplib
from email.mime.text import MIMEText

MAIL_HOST = 'smtp.163.com'
USERNAME = 'wu_yi_fan2013'
PASSWORD = '830824wujing'
MAIL_DOMAIN = '163.com'
MAIL_FROM = USERNAME + '@' + MAIL_DOMAIN
MAIL_TO = 'wujingjingjing@163.com'

# 在发送中文的时候，又遇到codec的问题
content = 'There is a meeting tomorrow afternoon. Do not forget !'

def send_email(to, subject, content) :
	msg = MIMEText(content)
	msg['Subject'] = subject
	msg['From'] = MAIL_FROM
	msg['To'] = MAIL_TO
	try:
		smtp = smtplib.SMTP(MAIL_HOST)
	except Exception as e:
		print('Connect to %s failed!' % MAIL_HOST)
		raise e
	print('Success to connect %s' % MAIL_HOST)

	try:
		smtp.login(USERNAME,PASSWORD)
	except Exception as e:
		print('Login Failed!')
		raise e
	print('Login Success!')
	
	try:
		smtp.sendmail(MAIL_FROM, to, content)
	except Exception as e:
		print('Send email Failed !')
		raise e
	print('Send email successfully!')

	smtp.quit()


if __name__ == '__main__':
	send_email(MAIL_TO, 'test email', content)