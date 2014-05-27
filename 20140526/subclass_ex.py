#coding:utf-8

import class_ex

class MySubClass(class_ex.MyClass):
	__doc__ = 'This a subclass which inherit MyClass !'

	__name__ = 'My custom subclass'

	def __init__(self, name, grade):
		class_ex.MyClass.__init__(self,name,grade)
		
	# __del__和__init__ , __str__ , __cmp__一样，也是一个基础函数，可以被重写
	# 当该类实例被回收前，将调用该函数，所以可以在这个函数中加入回收前需要做的事情
	def __del__(self):
		class_name = self.__class__.__name__
		print(class_name, ' will be destroyed soon!')

	# 和java中的String方法是一样的道理
	def __str__(self):
		return 'Hello world 2 !'

	def call_count(self):
		print('I am counting')



c1 = MySubClass('subclass1', '1')

c1.call_count()
print('c1 : ', c1)
print('__doc__ : ', c1.__doc__)
print('__name__ : ', c1.__name__)
print('__dict__ : ', MySubClass.__dict__)
# __bases__ 列出该类继承的所有基类
print('__bases__ ：', MySubClass.__bases__)



