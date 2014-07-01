#coding:utf-8

import ttk
import Tkinter

top = Tkinter.Tk()
ttk.Style().configure('MyButton',relief='flat',background='#ccc',padding=6)
# ttk.Button(top,text='MyButton',style='MyButton').pack()
ttk.Button(top,text='MyButton',command=top.quit).pack()

top.mainloop()