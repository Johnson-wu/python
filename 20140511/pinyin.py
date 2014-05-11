# -*- coding:utf-8 -*-

import os.path

class PinYin(object):
	def __init__(self, dict_file='word.data'):
		self.word_dict = {}
		self.dict_file = dict_file
		
	def load_word(self):
		if os.path.exists(self.dict_file):
			file = open(self.dict_file)
			for line in file.readlines():
				# print(line.split('    '), '\t', type(line.split('    ')), '\t', len(line.split('    ')))
				try:
					k, v = line.split('    ')
					self.word_dict[k] = v
				except:
					k, v = line.split('   ')
					self.word_dict[k] = v
			file.close()
		else:
			raise IOError('File not found !')
				
	def hanzi2pinyin(self, string=""):
		result = []
		
		# python3之后string都是以unicode编码的，所以这一步不需要，而且unicode这个内置的类型也已遗弃
		# if not isinstance(string, unicode):
			# string = string.decode('utf-8')
			
		for char in string:
			key = '%X' % ord(char) # HEX? 获取字符的编码，是十进制还是十六进制？
			# self.word_dict.get(key, char).split()[0]取出list的一个str元素，因为Str才有lower()方法，后面[0:-1]为去掉音调
			result.append(self.word_dict.get(key, char).split()[0][0:-1].lower()) 
		return result
		
	def hanzi2pinyin_split(self, string="", split=""):
		result = self.hanzi2pinyin(string)
		if split == "":
			return result
		else:
			# python3中有了变化 str.join(iterable)参数必须是一个遍历结构
			# return split.join('%s' % v for v in result) # 很方便的一个方法，直接将序列的值用某个字符串联起来
			return split.join('%s' % v[0:1] for v in result) # 稍微变化，就可以取得首拼。python的编码真的很简洁

PinYin()	
			
if __name__ == '__main__':
	test = PinYin()
	test.load_word()
	string = '世界您好啊'
	print('In: %s' % string)
	print('Out: %s' % str(test.hanzi2pinyin(string)))
	print('Out2: %s' % test.hanzi2pinyin_split(string, '-'))