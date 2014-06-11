#coding:utf-8

str1 = '你好啊'
print str1
print unicode('你好啊','utf-8')

# Decodes the object input and returns a tuple (output object, length consumed). 
# In a Unicode context, decoding converts a plain string to a Unicode object.
print str1.decode('utf-8') 
print '=================================='

str2 = u'你好啊' # str2 is a unicode object
print str2

print '=================================='
for s in str2:
	print s,ord(s),len(s)	# unicode 编码，对无论是字母还是中文都是占一个字节

print '=================================='
for s in str2:
	# ord() 只能接受长度为1的字符
	print s,ord(s.encode('utf-8')),len(s)	# UTF8 编码的中文占有三个字节
	print s,ord(s.encode('gbk')),len(s)	# GBK 编码的中文占有两个字节

