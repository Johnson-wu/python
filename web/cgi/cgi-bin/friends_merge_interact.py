#coding:utf-8

import cgi
# quote_plus 什么作用？没有用，也没有什么区别
from urllib import quote_plus

URL = '/cgi-bin/friends_merge_interact.py'
headers = 'Content-Type: text/html\n'

# 其中的input action是用来标识是否为formhtml的，同时必须有values，否则cgi在取值时不会取没有值的参数
formhtml = '''
<html><head><meta charset='utf-8'/><title>Friends CGI static Demo</title></head>
<body><h3>Friend list for users:<I>New User</I></h3>
<form action='/cgi-bin/friends_merge_interact.py'><B>Enter your name:</B>
<input type="hidden" name="action" value="edit"/>
<input type="text" name="person" value="%s" size="15" />
<p><B>How many friends do you have?</B>
%s</p><input type="submit"></form></body></html>'''

fradio = '<input type="radio" name="howmany" value="%s" %s>%s'

resulthtml = '''
<html><head><meta charset='utf-8'/>
<title>Friends CGI static Demo</title></head>
<body><h3>Friend list for:<I>%s</I></h3>
Your name is :<B>%s</B><p>
You have <B>%s</B> Friends
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

def showForm(who, howmany):
	fradios = []
	checked = ''
	for i in range(5):
		# assert type(howmany) is int, 'i is %s and howmany is %s , howmany type is not integer' % (i, howmany)
		if i == int(howmany):
			checked = 'checked="checked"'
		else:
			checked = ''
		radio = fradio % (str(i), checked, str(i))
		fradios.append(radio)
	print headers + formhtml % (who, ''.join(fradios))

def doResults(who, howmany):
	# url = URL + '?action=reedit&person=%s&howmany=%s' % (quote_plus(who), howmany)
	url = URL + '?action=reedit&person=%s&howmany=%s' % (who, howmany)
	print headers + resulthtml % (who, who, howmany, url)

def showErrors(message, who, howmany):
	url = URL + '?action=reedit&person=%s&howmany=%s' % (who, howmany)
	print headers + errorhtml % (message, url)

def process():
	error = ''
	form = cgi.FieldStorage()
	who = 'New User'
	howmany = 0

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
