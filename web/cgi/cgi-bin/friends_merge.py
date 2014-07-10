#coding:utf-8

import cgi

headers = 'Content-Type: text/html\n'

# 其中的input action是用来标识是否为formhtml的，同时必须有values，否则cgi在取值时不会取没有值的参数
formhtml = '''
<html><head><meta charset='utf-8'/><title>Friends CGI static Demo</title></head>
<body><h3>Friend list for users:<I>New User</I></h3>
<form action='/cgi-bin/friends_merge.py'><B>Enter your name:</B>
<input type="hidden" name="action" value="identifier"/>
<input type="text" name="person" value="New User" size="15" />
<p><B>How many friends do you have?</B>
%s</p><input type="submit"></form></body></html>'''

fradio = '<input type="radio" name="howmany" value="%s" %s>%s'

resulthtml = '''Content-Type: text/html\n
<html><head><meta charset='utf-8'/>
<title>Friends CGI static Demo</title></head>
<body><h3>Friend list for:<I>%s</I></h3>
Your name is :<B>%s</B><p>
You have <B>%s</B> Friends</body></html>
'''

def showForm():
	fradios = []
	checked = ''
	for i in range(5):
		if i == 0:
			checked = 'checked="checked"'
		else:
			checked = ''
		radio = fradio % (str(i), checked, str(i))
		fradios.append(radio)
	print headers + formhtml % (''.join(fradios))

def doResults(who, howmany):
	print resulthtml % (who, who, howmany)

def process():
	form = cgi.FieldStorage()

	who = ('person' in form) and form['person'].value or 'New User'
	howmany = ('howmany' in form) and form['howmany'].value or 0

	# 第一次体会到assert 对调试的作用，不然这里没法输出，也不知道错误具体信息
	# assert 'action' in form, 'action not in form %s' % form
	if 'action' in form:
		doResults(who, howmany)
	else:
		showForm()


if __name__ == '__main__':
	process()
