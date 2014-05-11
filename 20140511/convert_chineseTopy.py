# -*- code:utf-8 -*-

import sys,os
import re
import string

class CConvert:
	def __init__(self):
		self.has_shengdiao = False
		self.just_shengmu = False
		self.spliter = '-'
		
		# load data dictionary table
		try:
			fp = open(os.path.join(sys.path[0],'utils','convert-utf-8.txt'))
		except IOError:
			print("Can\'t load data from convert-utf-8.txt\nPlease make sure this file exists.")
			sys.exit(1)
		else:
			self.data = fp.read().decode('utf-8')
			fp.close()
	
	# convert single Unicode to Pinyin from index
	def getIndex(self, strIn):
		if strIn == ' ':
			return self.spliter
		if set(strIn).issubset("'\"`~!@#$%^&*()=+[]{}\\|;:,.<>/?"):
			return self.spliter
		if set(strIn).issubset("－—！#＃%％&＆（）*，、。：；？？　@＠＼{｛｜}｝~～‘’“”《》【】+＋=＝×￥·…　".decode("utf-8")):
			return ''
		pos = re.search("^"+strIn+"([0-9a-zA-Z]+)", self.data, re.M)
		if pos == None:
			return strIn
		else:
			if not self.just_shengmu:
				return pos.group(1)
			else:
				return pos.group(1)[:1]
		

	# convert Unicode sting to pinyin
	def convert(self, strIn):
		if self.spliter != '-' and self.spliter != '_' and self.spliter != ' ':
			self.spliter = '-'
		pinyin_list = []
		for c in strIn:
			print(c)
			pinyin_list.append(self.getIndex(c))
		pinyin=''
		for p in pinyin_list:
			if p == ' ':
				pinyin += self.spliter
				continue
			if len(p) < 2:	#
				pinyin += p + ' '
			else:
				if not self.has_shengdiao: # if don't have shengdiao , get list of p but the last character
					p = p[:-1]
					pingyin += self.spliter + p + self.spliter
		pinyin = pinyin.replace(' ', '')\
				.replace(self.spliter + self.spliter, self.spliter)\
				.strip(self.spliter+' ').replace(self.spliter+self.spliter,self.spliter)
		return pinyin
		
CConvert()
		