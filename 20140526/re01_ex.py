#coding:utf-8

import re

# match 与 search的区别：
# match 如果字符串的开始不符合正则表达式，则匹配失败，返回none
# search 匹配整个字符串，直到找到一个匹配，并返回一个matchobject, 否则才返回none

line = 'Cats are smarter than dogs'

# re.M 代表多行匹配，re.I 代表大小写不敏感
# mat = re.match(r'(.*) are (.*)', line, re.M|re.I)

# . 代表匹配任意字符，除了换行符
# 看效果，只是匹配出了（）里面的内容
mat = re.match(r'are (.*?) .*', line, re.M|re.I) 

if mat:
	# match.groups() 返回的是一个元组，而且该元组的下标比较特殊：是从1开始
	print(mat.groups(), len(mat.groups()))
	for i in range(len(mat.groups())):
		print(mat.group(i+1))
else:
	print('not match!')

print('============================')


sear = re.search(r'are (.*?) .*', line, re.M|re.I)
if sear :
	print(sear.groups())
	for i in range(len(sear.groups())):
		print(sear.group(i+1))
else:
	print('search not match!')

print('============================')

# 检索和替换
phone = '2014-05-26 # This is phone number.'

phone = re.sub(r'# .*', '', phone)
print(phone)

phone = re.sub(r'\D', '', phone, count=2)
print(phone)