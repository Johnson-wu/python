#coding:utf-8

import re
import os

# reg=r'(\d{1,2})/(\d{1,2})/(\d{2}|\d{4})$'

# result = re.sub(reg,r'\3/\2/\1','25/7/2014')

# print result

with os.popen('tasklist /nh','r') as f:
	for eachline in f:
		# print re.split(r'\s\s+|\t',eachline.strip())
		print re.findall(r'(\w+.?\w+)\s\s+(\d+) (\w+)\s\s+(\d+)\s\s+(.+ k)',eachline.strip())
		# print re.findall(r'([\w.]+(?: [\w.]+)*)\s\s+(\d+) (\w+)\s\s+(\d+)\s\s+([\d,]+ K)',eachline.rstrip())