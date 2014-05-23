#coding:utf-8

# 一定要注意global summary的用法！！！
# 之前是用把summary当作参数传给start_count()，结果发现在递归时，前一个文件计算的数值会被清零。
import os
import tokenize
import time
import sys,imp 

summary = 0

def start_count(path):
	global summary	
	file_list = os.listdir(path)
	for f in file_list:
		absolute_path = path + '\\' + f
		if os.path.isdir(absolute_path):
			start_count(absolute_path)
		else:
			count_code_line(absolute_path)
		# print(summary)
	

def count_code_line(file):
	global summary
	basename = os.path.split(file)[1]
	# print(file)
	ext = os.path.splitext(basename)
	if ext[1] in ('.py','.html'):
		codec = judge_codec(file)
		# print('codec : %s' % codec)
		hand = open(file,encoding=codec)
		while True:
			if hand.readline():
				summary += 1
				# print('summary : %s' % summary)
			else:
				break

def judge_codec(file):
	hand = open(file,'rb')
	li = tokenize.detect_encoding(hand.readline)
	return li[0]


time1 = time.time()
# start_count('E:\\Github\\web-development')
# start_count('E:\\Github\\python')
# start_count('E:\\Github\\Python-Tutorial-Vamei')
# start_count('E:\\Github\\Protocol-Forest-Vamei')
start_count('E:\\Github')
print('summary : %s' % summary)
time2 = time.time()
print(time2-time1)

# Return the name of the current default string encoding used by the Unicode implementation.
imp.reload(sys)
print(sys.getdefaultencoding())

# sublime为什么打不出中文？？？在cmd里面直接跑是可以打印出中文的
# print('中文')
# print(u'用时：%s 秒' % (time2-time1))

