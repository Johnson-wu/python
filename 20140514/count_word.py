# -*- coding:utf-8 -*-
# 计算文档中的单词分别出现次数
# ???为什么把空格也计数了？

import os
import sys
import operator
import re

def count_word(filepath):
	absolutepath = os.path.join(sys.path[0], filepath)
	# print(absolutepath)
	file = open(absolutepath)
	count_dict = {}
	count_dict["空格"] = 0
	regex = re.compile(r'[^a-zA-Z]')
	# Method : two
	for word in regex.split(file.read()):
		# 加上这个判断，可以过滤掉最大的计数
		# if word == '': continue  # 这个要如何用正则去掉?
		if re.match(r'\S',word): count_dict["空格"] += 1 # 这样也匹配不了''
			
		if word in count_dict:
			# count_dict[word] += count_dict[word] + 1 #就是这里导致计数不对
			count_dict[word] += 1
		else:
			count_dict[word] = 1
		
	# Method : One
	# regex = re.compile(r'[#_\-*\[\]\\/\'\(\)\%\\\n\.:,0123456789]')
	# dealed_text = re.sub(regex, ' ', file.read()) # 将不需要的特殊字符替换成' '
	# for word in dealed_text.split(): # str.split()默认用的是' '来分割
		# if word in count_dict: # 判断字典中是否存在某个key，若直接dic[key],如果没有该key,则会报KeyError
			# count_dict[word] += 1
			# # print('Add----%s : %d' % (word,count_dict[word]))
		# else:
			# count_dict[word] = 1
			# # print('Init----%s : %d' % (word,count_dict[word]))
	
	file.close()	
	return count_dict
	
	
def sort_count_dict(dict):
	# sorted的第一个参数需为list或iterable，直接用dict不行
	# sorted_dict = sorted(dict, key=operator.itemgetter(1), reverse=True)
	sorted_dict = sorted(dict.items(), key=operator.itemgetter(1), reverse=True)
	# print('Key:%s , Value:%d' % (k,v) for k,v in sorted_dict) # 打出了对象，内容没能打出来
	for k,v in sorted_dict:
		# pass
		print('Key:%s--Value:%d' % (k,v))
	
	
dict = count_word('test.txt')
sort_count_dict(dict)