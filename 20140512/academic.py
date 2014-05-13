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
	
	# ��ӡ��ϸ�������
	curs = 0
	sumary = 0
	for num in sb[::-1]:  #[::]����������Ϊ����������Ϊ���򸺣��磺2��������ÿ��һλȡֵ��-2��������ÿ��һλȡֵ����[::-1]ʵ�����ִ���ת
		tmpsum = str(int(num)*a)
		print_sum_process(resultlength, tmpsum, curs)
		
		# �ֶ��ӳ���ֵ
		if curs != 0:
			sumary += int(num)*a*(10**curs)	# Ҫע�⣬���ݣ�����10*curs
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



