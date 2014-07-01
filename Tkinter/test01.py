#coding:utf-8

from Tkinter import *

class App(Frame):
	def __init__(self,master=None):
		Frame.__init__(self,master)
		self.pack()


MyApp = App()

MyApp.master.title('customize frame...')
MyApp.master.minsize(500,250)
MyApp.master.maxsize(1000,500)

MyApp.mainloop()