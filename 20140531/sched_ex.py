#coding:utf-8

import datetime
import sched,time

# 计算某一天的日期
def count_someday():
	today = datetime.date.today()
	print(today)
	# timedelta : this object represents a duration , the difference between two dates or times
	yesterday = today - datetime.timedelta(days=1)
	print(yesterday)
	print(datetime.timedelta(days=3))

	# the day of the week, from 0 to 6
	print('Today is %s of the week.' % today.weekday())

def sche_print(content):
	print(content)



if __name__ == '__main__':
	count_someday()

	s = sched.scheduler(time.time, time.sleep)

	# 2 秒后向控制台输出
	s.enter(2,3,sche_print,('print priority every 2 seconds.',))
	s.run()

	