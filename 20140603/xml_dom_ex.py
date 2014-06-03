#coding:utf-8
# 使用dom解析xml,有两个模块可以使用，一个是传统的xml.dom,一个是xml.dom.minidom
# there are three definition need to be understood : Node , Document , Element
# DOM xml中每一个成分都一个节点：
# 	整个文档是一个节点；每个XML标签是一个节点；包含在XML元素中的文本是文本节点;每一个XML属性是一个属性节点；注释属于注释节点；

import xml.dom.minidom as minidom

DOMTree = minidom.parse('test.xml')
# return the one and only root element
collection = DOMTree.documentElement

if collection.hasAttribute('shelf'):
	print('Root element\'s attribute is %s' % collection.getAttribute('shelf'))

# getElementsByTagName('tagname') will return all childnodes named 'tagname' and type is list
movies = collection.getElementsByTagName('movie')

for movie in movies:
	if movie.hasAttribute('title'):
		print('movie\'s title is %s' % movie.getAttribute('title'))

	# Same as equivalent method in the Document class.
	type = movie.getElementsByTagName('type')[0]
	# Node.childNodes: return A list of nodes contained within this node.
	print('movie type is : %s' % type.childNodes[0].data)




