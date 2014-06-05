#coding:utf-8

import tkinter as tk

class Application(tk.Frame):
	def __init__(self, master=None):
		tk.Frame.__init__(self,master)
		# pack（）是用来管理和显示组件
		self.pack()
		self.createWidgets()

	def createWidgets(self):
		self.hello = tk.Button(self,text='Click Me')
		self.hello['command'] = self.sayHello
		self.quit = tk.Button(self,text='Quit',fg='red',command=root.destroy)
		self.hello.pack(side='left')
		self.quit.pack(side='right')

	def sayHello(self):
		print('Hello World !')


root = tk.Tk()
root.geometry('400x300')	# 这里使用400*300还报错，一定要400x300
app = Application(root)
# 进入消息循环
app.mainloop()