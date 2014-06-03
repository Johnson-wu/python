#coding:utf-8
# python 解析xml

import xml.sax

class MovieHandler(xml.sax.handler.ContentHandler):
	def __init__(self):
		self.CurrentData = ''
		self.type = ''
		self.format = ''
		self.year = ''
		self.rating = ''
		self.stars = ''
		self.description = ''

	# 遇到元素开始标签时触发
	def startElement(self, tag, attributes):
		print('============Start Element===========')
		self.CurrentData = tag
		if tag == 'movie':
			print('******movie*******')
			title = attributes['title']
			print('Title is : %s' % title)
		else:
			print('start element is %s' % tag)

	# 遇到元素结束标签时触发	 
	def endElement(self, tag):
		if self.CurrentData == 'type':
			print('Type is : %s' % self.type)
		elif self.CurrentData == 'format':
			print('Format is ', self.format)
		elif self.CurrentData == 'year':
			print('Year is ', self.year)
		elif self.CurrentData == 'rating':
			print('Rating is ', self.rating)	
		elif self.CurrentData == 'stars':
			print('Stars is ', self.stars)
		elif self.CurrentData == 'description':
			print('Description is ', self.description)
		# self.CurrentData = ''
		print('============End Element===========')

	# 内容事件处理: 遇到字符数据时触发,这个字符数据指所有字符数据，标签也是字符数据,所以每行内容实际会触发三次这个方法（前后标签元素各一次，中间内容一次）
	# 并且字符数据还可能包括空格
	def characters(self, content):
		print('start to dealing with characters')
		if self.CurrentData == 'type':
			# 吐血，前面赋值一直用的==，难怪赋值赋不上
			self.type = content
		elif self.CurrentData == 'format':
			self.format = content
		elif self.CurrentData == 'year':
			self.year = content
		elif self.CurrentData == 'rating':
			self.rating = content
		elif self.CurrentData == 'stars':
			self.stars = content
		elif self.CurrentData == 'description':
			self.description = content
		# print('CurrentData is : %s and content is %s' % (self.CurrentData,content))


if __name__ == '__main__':
	# create and return a 'xml.sax.xmlreader.XMLReader' object.
	parser = xml.sax.make_parser()

	# Set the featurename to value. If the feature is not recognized, SAXNotRecognizedException is raised.
	# If the feature or its setting is not supported by the parser, SAXNotSupportedException is raised.
	# xml.sax.handler.feature_namespaces 
	# value: "http://xml.org/sax/features/namespaces"
	# true: Perform Namespace processing.
	# false: Optionally do not perform Namespace processing (implies namespace-prefixes; default).
	# access: (parsing) read-only; (not parsing) read/write
	# 看样子feature_namespaces相当于html中的Doctype的作用。
	# 本例中把这个域名设为0，即为false
	parser.setFeature(xml.sax.handler.feature_namespaces, 0)

	handler = MovieHandler()
	parser.setContentHandler(handler)

	parser.parse('test.xml')

