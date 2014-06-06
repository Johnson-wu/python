#coding:utf-8
# 用python维护Window环境变量

import sys,os
# from subprocess import check_all

# 判断python版本。winreg用来访问 Windows registry API to Python
if sys.hexversion > 0x03000000:
	import winreg
else:
	import _winreg as winreg

# Utility class to get/set windows env variable
class Win32Env:

	def __init__(self, scope):
		# Assert statements are a convenient way to insert debugging assertions into a program.
		# assert 是一种防御性编程形式，预先知道scope的取值范围，便可以用assert来加入断点，超出会抛出AssertionError,可以Try处理
		# 当然也可以用判断语句来判断范围，但是不优美
		assert scope in ('user','system')
		self.scope = scope
		if scope == 'user':
			self.root = winreg.HKEY_CURRENT_USER
			self.subkey = 'Environment'
		else:
			self.root = winreg.HKEY_LOCAL_MACHINE
			self.subkey = r'SYSTEM\\CurrentControlSet\\Control\\Session Manager\\Environment'

	def getEnv(self, name):
		# Opens the specified key, returning a handle object.
		key = winreg.OpenKey(self.root, self.subkey, 0, winreg.KEY_READ)
		try:
			# Retrieves the type and data for a specified value name associated with an open registry key.
			# and The result is a tuple of 2 items:
			# 		index 0 : The value of the registry item.
			# 		index 1 : An integer giving the registry type for this value
			value, _ = winreg.QueryValueEx(key, name)
		except Exception as e:
			raise e
		return value

	def setEnv(self, name, value):
		key = winreg.OpenKey(self.root, self.subkey, 0, winreg.KEY_ALL_ACCESS)
		winreg.SetValueEx(key, name, 0, winreg.REG_EXPAND_SZ, value)
		winreg.CloseKey(key)



if __name__ == '__main__':
	env = Win32Env('system')
	print(env.getEnv('PATH'))

	print('=============================================')

	env2 = Win32Env('user')
	print(env2.getEnv('TEMP'))
	# os.path.expanduser(path) 将return参数中的path,如果path以~开头，则~会被替换会user‘s home directory,如下面
	env2.setEnv('TEST', os.path.expanduser(r'~\tests'))
	print(env2.getEnv('TEST'))

	env2 = Win32Env('test')



