#-*-coding:utf-8-*-
#遍历某一路径下的所有文件，并将文件的绝对路径写入文件

import os
import os.path
import sys

def print_inventory_tree(path):
	self_path = sys.path[0]  # 获取当前pyton脚本的路径
	print(self_path)
	inventory = []
	file = open(self_path + '/' + 'inventory.txt','w') # 如果文件不存在，会创建
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
		
# 利用os.walk()来遍历某个目录
def iterator_inventory2(path):
	for current_path, dir_list, file_list in os.walk(path):
		print('%s %s %s' % (current_path,dir_list,file_list))
		# for filename in file_list:
			# print(os.path.join(current_path,filename))

# print_inventory_tree('E:/study')

iterator_inventory2('E:\study')