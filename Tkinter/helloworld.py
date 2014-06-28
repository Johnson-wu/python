import Tkinter

def resize(ev=None):
	label.config(font='Helvetica -%d bold' % scale.get())

root = Tkinter.Tk()
root.geometry('250x150')

label = Tkinter.Label(root, text='Hello World !', font='Helvetica -12 bold')
label.pack(fill=Tkinter.Y,expand=1)

scale = Tkinter.Scale(root, from_=5, to=40, orient='horizontal', command=resize)
scale.set(12)
scale.pack(fill=Tkinter.X,expand=1)

# button = Tkinter.Button(root, text='Quit', command=root.quit, bg='red', fg='white')
button = Tkinter.Button(root, text='Quit', command=root.quit, activeforeground='white', activebackground='red')
button.pack(fill=Tkinter.X)
# button.pack(fill=Tkinter.X, expand=1)
Tkinter.mainloop()