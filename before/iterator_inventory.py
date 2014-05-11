#-*-coding:utf-8-*-
#����ĳһ·���µ������ļ��������ļ��ľ���·��д���ļ�

import os
import os.path
import sys

def print_inventory_tree(path):
	self_path = sys.path[0]  # ��ȡ��ǰpyton�ű���·��
	print(self_path)
	inventory = []
	file = open(self_path + '/' + 'inventory.txt','w') # ����ļ������ڣ��ᴴ��
	iterator_inventory(path,inventory,file)
	file.close()
	
	

def iterator_inventory(path,inventory,file):
	for com_path in os.listdir(path):
		obsolute_path = path + '/' + com_path
		inventory.append(obsolute_path)
		file.write(obsolute_path +'\n')
		# print(obsolute_path)
		if os.path.isdir(obsolute_path):
			iterator_inventory(obsolute_path,inventory,file)
		else:
			continue
		
# ����os.walk()������ĳ��Ŀ¼
def iterator_inventory2(path):
	for current_path, dir_list, file_list in os.walk(path):
		print('%s %s %s' % (current_path,dir_list,file_list))
		# for filename in file_list:
			# print(os.path.join(current_path,filename))

# print_inventory_tree('E:/study')

iterator_inventory2('E:\study')