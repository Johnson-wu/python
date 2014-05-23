#coding:utf-8

# yield : 通过在函数中加入yield，可以控制函数运行的阶段和时机。
# 比如：当函数运行到一半yield一下，将函数挂起，完成其他事情后再回头继续运行
# 但是，关键的yield的运用场景是在什么地方？

def f():
	for i in range(4):
		yield i*2
		# return

y = f()	# f()将返回一个generator对象

for i in range(4):
	print(next(y))	# python3 后,y.next()被废弃了，应该用next(y)

delimeter = '======================'
print(delimeter)

def f1():
	x = 'lo'
	y = 'li'
	z = (yield x) + (yield y)
	print(z)

y = f1()
# print(next(y))
# print(next(y))

# print(next(y)) # 抛出异常TypeError: unsupported operand type(s) for +: 'NoneType' and 'NoneType'

# 会打出和之前两次next(y)一样的效果，why???
print(y.send(None))
print(y.send('kawaii too')) # send 进去的值呢？如何被处理的？

