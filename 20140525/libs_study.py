#coding:utf-8

# python 用来处理时间的常用模块有datetime、time、calendar
import calendar
import time


# 获取某月日历
def show_calendar():
	cal = calendar.month(2014,5)
	print(cal)


def change_number(num):
	num += 1
	print('in def num is %d' % num)


def change_str(str):
	str = 'inner'
	print('in def str is %s' % str)

def change_list(list):
	list.append([4,5])
	print('in def list is %s' % list)


if __name__ == '__main__':
	separator = '=========================='
	show_calendar()

	print('Time.time() : %s ' % time.time())
	# print(time.localtime(time.time()))

	# class time.struct_time 
	# 		The type of the time value sequence returned by gmtime(), localtime(), and strptime().
    # 		It is an object with a named tuple interface: values can be accessed by index and by attribute name. 
	# localtime() 返回一个struct_time
	print('Time.localtime : %s ' % str(time.localtime()))
	# asctime()返回格式化时间，参数必须为 tuple or struct_time
	print('Get format time : %s' % time.asctime(time.localtime()))
	print('Time.gmtime() : %s' % str(time.gmtime()))
	print('Get format time : %s' % time.asctime(time.gmtime()))


	# 由下面三个列子可见，数字和字符串是不可变的，在传参时，实际是将值所在的内存复制了一份，所以在函数中改变后，对原始的变量没有影响
	# 而list是将变量的引用传递进函数，所以当函数中改变后，原始变量也相应改变
	print(separator)
	num = 0
	print('before change num is %d ' % num)
	change_number(num)
	print('after change num is %d' % num)

	print(separator)
	str = 'external'
	print('before change str is %s ' % str)
	change_str(str)
	print('after change str is %s' % str)

	print(separator)
	li = [1,2,3,4,5]
	print('before change list is %s' % li)
	change_list(li)
	print('after change list is %s' % li)

	print(separator)
	sum = lambda x, y : x + y
	print(sum(2,3))