# -*- coding:utf-8 -*-

def bigmul(a,b):
	sa = str(a)
	sb = str(b)
	resultlength = len(sa)+len(sb)
	sum = a * b
	sumstr = str(sum)
	
	print('\n' + ' '*len(sb) + sa)
	print('*' + ' '*(len(sa)-1) + sb)
	print('-' * resultlength)
	
	# 打印详细计算过程
	curs = 0
	sumary = 0
	for num in sb[::-1]:  #[::]第三个参数为步进，可以为正或负，如：2代表正序每隔一位取值，-2则是逆序每隔一位取值。而[::-1]实现了字串反转
		tmpsum = str(int(num)*a)
		print_sum_process(resultlength, tmpsum, curs)
		
		# 手动加出总值
		if curs != 0:
			sumary += int(num)*a*(10**curs)	# 要注意，是幂，不是10*curs
			# print('%d %d %d' % (int(num), curs, int(num)*a*(10**curs)))
		else:
			sumary += int(num)*a
			# print('%d %d %d' % (int(num), curs, int(num)*a))
			
		curs += 1
		
	print('-' * resultlength)
	print(' '*(resultlength-len(sumstr)) + sumstr)
	print(sumary)
	
	
def print_sum_process(resultlength, tmpsum, curs):
	print(' '*(resultlength-len(tmpsum)-curs) + tmpsum + ' '*curs)
	
	
if __name__ == '__main__':
	bigmul(123, 123456789)



