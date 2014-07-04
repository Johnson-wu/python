#coding:utf-8

teams = [['法国','德国'],['巴西','哥伦比亚'],['阿根廷','比利时'],['荷兰','哥斯达黎加']]


def gerNewList(list1,list2):
	newList = []
	for i in range(len(list1)):
		for j in range(len(list2)):
			tmp = list1[i] + ',' + list2[j]
			newList.append(tmp)	
	return newList

def gerGroup(team):
	result = []
	for i in range(1,len(team)):
		if i == 1:
			result = gerNewList(team[i-1],team[i])
		else:
			result = gerNewList(result,team[i])
	return result

if __name__ == '__main__':
	res = gerGroup(teams)
	for i in range(len(res)):
		print res[i].decode('utf-8').encode('utf-8')
