#coding:utf-8

# 使用walk来遍历path：测试下来效率比之前的方法慢个0.015s
import os
import tokenize
import time
import re

summary = 0
EXT_LIST = ['.py','.html','.java']

def start_count_by_walk(path):
	global summary
	for current_path, dir_list, file_list in os.walk(path):
		for f in file_list:
			if os.path.splitext(f)[1] in EXT_LIST:
				file_path = current_path + '\\' + f
				count_code_line(file_path)

def count_code_line(path):
	global summary
	codec = judge_codec(path)
	hand = open(path,encoding=codec)
	while hand.readline():
		summary += 1

def judge_codec(file):
	hand = open(file,'rb')
	li = tokenize.detect_encoding(hand.readline)
	return li[0]


time1 = time.time()
print('start...')
start_count_by_walk('E:\\Github')
print('summary : %s' % summary)
time2 = time.time()
print('end : %s' % (time2-time1))




