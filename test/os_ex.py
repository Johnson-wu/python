import os

class Test:
	def call_sys(self, host):
		print host
		os.system('ping "%s"' % host)


if __name__ == '__main__':
	t = Test()
	t.call_sys('www.baidu.com')