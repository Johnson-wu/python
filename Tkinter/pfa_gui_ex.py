#coding:utf-8

from functools import partial
import Tkinter
from tkMessageBox import showinfo,showwarning,showerror

WARN = 'warn'
CRIT = 'crit'
REGU = 'regu'

SIGNS = {
	'do not enter': CRIT,
	'railroad crossing': WARN,
	'55\nspeed limit': REGU,
	'wrong way': CRIT,
	'merging traffic': WARN,
	'one way': REGU
}

critCB = lambda: showerror('Error', 'Error Button Pressed!')
warnCB = lambda: showwarning('warning','warning Button Pressed!')
infoCB = lambda: showinfo('Info','Info Button Pressed!')

root = Tkinter.Tk()
root.title('Road Signs')
root.geometry('250x200')
Tkinter.Button(root, text='QUIT', command=root.quit, bg='red', fg='white').pack()

MyButton = partial(Tkinter.Button,root)
CritButton = partial(MyButton, command=critCB, bg='white', fg='red')
WarnButton = partial(MyButton, command=warnCB, bg='goldenrod1')
ReguButton = partial(MyButton, command=infoCB, bg='white')

for eachSign in SIGNS:
	print eachSign
	signType = SIGNS[eachSign]
	# str.title() 
	# Return a titlecased version of the string where words start with an uppercase character and the remaining characters are lowercase.
	# 可以如此理解：%r 打印的是对象,是可以组成一个表达式的; %s打印的是可打印的字串内容
	# 官方手册解释：The difference with repr(object) is that str(object) does not always attempt to return a string that is acceptable to eval(); 
	# its goal is to return a printable string. If no argument is given, returns the empty string, ''.
	# cmd = '%sButton(text=%r%s).pack(fill=Tkinter.X,expand=True)' % (
	# 	signType.title(), eachSign,
	# 	'.upper()' if signType == CRIT else '.title()')  # 直接插入条件表达式

	cmd = '%sButton(text=%r%s).pack(fill=Tkinter.X,expand=True)' % (
		signType.title(), eachSign,
	    signType == CRIT and '.upper()' or '.title()')
	eval(cmd)

root.mainloop()