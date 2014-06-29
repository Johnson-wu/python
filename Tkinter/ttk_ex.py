#coding:utf-8

import Tkinter
import ttk

root = Tkinter.Tk()

Tkinter.Label(root, text='Animals(in pairs;min:pair,max:dozen').pack()

frame1 = Tkinter.Frame(root)
Tkinter.Label(frame1, text='Number:').pack(side=Tkinter.LEFT)
Tkinter.Spinbox(frame1, from_=2, to=12, increment=2, font='Helvetica -14 bold').pack(side=Tkinter.RIGHT,fill=Tkinter.X,expand=1)
frame1.pack()

frame2 = Tkinter.Frame(root)
Tkinter.Label(frame2, text='Type:').pack(side=Tkinter.LEFT)
ttk.Combobox(frame2, value=('dog','cat','hamster','python')).pack(side=Tkinter.RIGHT,fill=Tkinter.X,expand=1)
frame2.pack()

Tkinter.Button(root, text='Quit', command=root.quit).pack()

root.mainloop()