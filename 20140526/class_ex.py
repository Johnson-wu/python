#coding:utf-8

class MyClass():
	# 在属性和方法名前加上'__',就可将其转变为私有
	# 私有属性，实例对象及子类都无法直接访问
	__private_counter = 0

	__doc__ = 'This a custom class for test !'

	__name__ = 'My custom class'

	def __init__(self, name, grade):
		self.name = name
		self.grade = grade

	# __del__和__init__ , __str__ , __cmp__一样，也是一个基础函数，可以被重写
	# 当该类实例被回收前，将调用该函数，所以可以在这个函数中加入回收前需要做的事情
	def __del__(self):
		class_name = self.__class__.__name__
		print(class_name, ' will be destroyed soon!')

	# 和java中的String方法是一样的道理
	def __str__(self):
		return 'Hello world !'

	# 私有方法，实例对象及子类无法直接访问
	def __count(self):
		self.__private_counter += 1

	def call_count(self):
		self.__count()
		print(self.__private_counter)



# 模块中这些直接调用的方法，要放在下面的if语句中，否则当其他模块引用该模块时，就会这些方法自动执行一遍
# c1 = MyClass('class1', '1')
# c1.call_count()
# print('c1 : ', c1)
# print('__doc__ : ', c1.__doc__)
# print('__name__ : ', c1.__name__)
# print('__dict__ : ', MyClass.__dict__)


if __name__ == '__main__':
	c1 = MyClass('class1', '1')
	c1.call_count()
	print('c1 : ', c1)
	print('__doc__ : ', c1.__doc__)
	print('__name__ : ', c1.__name__)
	print('__dict__ : ', MyClass.__dict__)




# c1.__count()
# print(c1.__private_counter)

