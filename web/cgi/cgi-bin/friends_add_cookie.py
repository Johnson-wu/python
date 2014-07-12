#coding:utf-8

import cgi
# quote_plus 什么作用？没有用，也没有什么区别
from urllib import quote_plus
from StringIO import StringIO
from os import environ

URL = '/cgi-bin/friends_add_cookie.py'
headers = 'Content-Type: text/html\n'

# 其中的input action是用来标识是否为formhtml的，同时必须有values，否则cgi在取值时不会取没有值的参数
formhtml = '''
<html><head><meta charset='utf-8'/><title>Friends CGI static Demo</title></head>
<body><h3>Friend list for users:<I>New User</I></h3>
<form action='/cgi-bin/friends_add_cookie.py'>
<input type="hidden" name="action" value="edit"/>
<h2>My cookie setting</h2>
<B>Enter your cookie:</B><input type="text" name="cookie" value="%s"/><I>(Optional)</I><B>%s</B><br/>
<B>Enter your name:</B><input type="text" name="person" value="%s" size="15" />
<p><B>How many friends do you have?</B>
%s</p>
<input type="file" name="upfile" size="45"/>
<input type="submit"></form></body></html>'''

fradio = '<input type="radio" name="howmany" value="%s" %s>%s'

resulthtml = '''
<html><head><meta charset='utf-8'/>
<title>Friends CGI static Demo</title></head>
<body><h3>Friend list for:<I>%s</I></h3>
Your name is :<B>%s</B><p>
You have <B>%s</B> Friends
<p><B>FileName : %s</B><br/>
Contents:</h3>
<pre>%s</pre></p>
<p>click <a href="%s">here</a> to reedit info</p></body></html>
'''

errorhtml = '''
<html><head><meta charset='utf-8'/>
<title>Friends CGI static Demo</title></head>
<body><h2>Error</h2>
<B>%s</B><br/>
<!--<input type="button" value="Back" onclick="window.history.back()"/>-->
<p>click <a href="%s">here</a> to reedit info</p>
</body></html>
'''

cookies = {}
fpipe = ''
fname = ''

def setCookie():
	# assert not cookies, cookies
	for cookie in cookies.keys():
		print 'Set-Cookie: %s=%s;path=/' % (cookie,cookies[cookie])

def getCookie():
	# assert 'HTTP-COOKIE' in environ, environ
	if 'HTTP-COOKIE' in environ:
		cookies = [x.strip() for x in environ['HTTP-COOKIE'].split(';')] 
		return '--'.join(cookies)

def showForm(who, howmany):
	fradios = []
	checked = ''
	cookie = getCookie()
	showMSG = 'There is no cookie' if not cookie else ''

	for i in range(5):
		# assert type(howmany) is int, 'i is %s and howmany is %s , howmany type is not integer' % (i, howmany)
		if i == int(howmany):
			checked = 'checked="checked"'
		else:
			checked = ''
		radio = fradio % (str(i), checked, str(i))
		fradios.append(radio)
	print headers + formhtml % (cookie, showMSG, who, ''.join(fradios))

def doResults(who, howmany):
	# url = URL + '?action=reedit&person=%s&howmany=%s' % (quote_plus(who), howmany)
	setCookie()
	data = fpipe.read(4096)
	if data:
		filedata = data
	else:
		filedata = 'File transfer error'

	url = URL + '?action=reedit&person=%s&howmany=%s' % (who, howmany)
	print headers + resulthtml % (who, who, howmany, fname, filedata, url)

def showErrors(message, who, howmany):
	url = URL + '?action=reedit&person=%s&howmany=%s' % (who, howmany)
	print headers + errorhtml % (message, url)

def process():
	error = ''
	form = cgi.FieldStorage()
	who = 'New User'
	howmany = 0

	cookies['friends'] = form['cookie'].value.strip() if 'cookie' in form else ''

	if 'person'	in form:
		who = form['person'].value
	else:
		# assert 'person' in form, 'person not in form %s' % form
		if 'action' in form and form['action'].value == 'edit':
			error = 'Please enter your name !'
		else:
			who = 'New User'

	if 'howmany' in form:
		howmany = form['howmany'].value
	else:
		# assert 'howmany' in form, 'howmany not in form %s' % form
		if 'action' in form and form['action'].value == 'edit':
			error = 'Please enter your friends number !'
		else:
			howmany = 0

	global fpipe, fname	
	if 'upfile' in form:
		upfile = form['upfile'] 
		fname = upfile.value or ''
		# upfile.file是什么？没有这个属性！
		assert upfile.file, upfile.filename
		if upfile.file:
			 fpipe = upfile.file
		else:
			 fpipe = StringIO('no data transfered')
	else:
		fpipe = StringIO('no file')
		fname = ''

	# assert not error, error
	if not error:
		if 'action' in form and form['action'].value != 'reedit':
			doResults(who, howmany)
		else:
			showForm(who, howmany)
	else:
		showErrors(error, who, howmany)

if __name__ == '__main__':
	process()
