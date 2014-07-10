#coding:utf-8

import cgi

# resulthtml = '''
# Content-Type: text/html\n
# <html>\n
# 	<head>\n
# 		<meta charset='utf-8'/>\n
# 		<title>Friends CGI static Demo</title>\n
# 	</head>\n
# 	<body>\n
# 		<h3>Friend list for:<I>%s</I></h3>\n
# 		Your name is :<B>%s</B><p>\n
# 		You have <B>%s</B> Friends\n	
# 	</body>\n
# </html>
# '''

# 编写html页面时，不能用上面的标签之间加回车的方式，这样会返回plain text，浏览器当文本处理了
# 但是HTTP HEADers 与 html之间必须换行，以便浏览器区分
resulthtml = '''Content-Type: text/html\n
<html><head><meta charset='utf-8'/>
<title>Friends CGI static Demo</title></head>
<body><h3>Friend list for:<I>%s</I></h3>
Your name is :<B>%s</B><p>
You have <B>%s</B> Friends</body></html>
'''

form = cgi.FieldStorage()
# who = form['person']    # 返回的是instances of FieldStorage or MiniFieldStorage，包含了key和value
who = form['person'].value
howmany = form['howmany'].value
print resulthtml % (who, who, howmany)