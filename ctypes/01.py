#coding:utf-8

from ctypes import *

DELIMETER = '============================\n'

class Bottle(object):
	def __init__(self, number):
		self._as_parameter_ = number


if __name__ == '__main__':
	pr = windll.msvcrt.printf
	pr('Hello %s !\n', 'World')
	pr('Hello %S !\n', u'World')
	pr('Hello Robot NO.%d !\n', 1)

	# all Python types except integers, strings, and unicode strings have to be wrapped 
	# in their corresponding ctypes type, so that they can be converted to the required C data type
	pr('Hello Robot NO.%f !\n', c_float(1.2))
	pr('Hello Robot NO.%f !\n', c_double(1.2))

	# 同样自定义的类参数也是integer,string,unicode string,否则也要进行包装包装
	bottle = Bottle(30)
	pr('There are %d bottles of beer !\n', bottle)

	# 注意下面两者打印顺序
	pr(DELIMETER) 
	# print DELIMETER

	strchr =  windll.msvcrt.strchr
	pr(strchr('hello world!\n', ord('w')))
	# strchr.restype = c_char_p
	# pr(strchr('hello world!\n', ord('w')))

