#coding:utf-8

import Tkinter 
import ttk
from functools import partial

WIDGETS_DICT = {
	'IDCard Type': ['证件类型:','combobox',(0,0),(0,1)],
	'IDCard Number': ['证件号码:','text',(0,2),(0,3)],
	'Name': ['姓  名 :','text',(1,0),(1,1)],
	'PinYin': ['首  拼 :','text',(1,2),(1,3)],
	'Gender': ['性  别 :','combobox',(2,0),(2,1)],
	'Brithday': ['出生日期:','text',(2,2),(2,3)],
	'Address': ['地  址 :','text',(3,0),(3,1)],
	'Phone': ['联系方式:','text',(3,2),(3,3)],
	'Status': ['状  态 :','combobox',(4,0),(4,1)],
	'Cost': ['挂号费:','combobox',(4,2),(4,3)],
	'Reg Type': ['类  别 :','combobox',(5,0),(5,1)],
	'Specialty': ['科  室 :','combobox',(5,2),(5,3)],
	'Doctor': ['医  生 :','combobox',(6,0),(6,1)],
	'Insurance Type': ['医保类型:','combobox',(6,2),(6,3)]
}


def register():
	pass
	

def guiGeneratorByPack(master=None):
	frames = []
	frame01 = Tkinter.Frame(master, width=100, height=500, bg='green')
	frames.append(frame01)
	frame02 = Tkinter.Frame(master, width=200, height=500, bg='red')
	frames.append(frame02)
	frame03 = Tkinter.Frame(master, width=100, height=500, bg='green')
	frames.append(frame03)
	frame04 = Tkinter.Frame(master, width=200, height=500, bg='red')
	frames.append(frame04)

	frame05 = Tkinter.Frame(master, bg='yellow')
	frame05.pack(side='bottom')

	for frame in frames:
		frame.pack(side=Tkinter.LEFT)

	MyLabel01 = partial(Tkinter.Label, frame01)
	cardType_lb = partial(MyLabel01, text='IDCard')
	cardType_lb().pack(side='top')	# 注意cardType_lb()后面的()必须加上，不然报错AttributeError: 'functools.partial' object has no attribute 'pack'
	idNumber_lb = partial(MyLabel01, text='IDNumber')
	idNumber_lb().pack(side='top')

	confirm_btn = Tkinter.Button(frame05, text='Confirm', command='')
	quit_btn = Tkinter.Button(frame05, text='Cancel', command=master.quit)
	quit_btn.pack(side=Tkinter.RIGHT,expand=1)
	confirm_btn.pack(side=Tkinter.RIGHT,expand=1)
	

def guiGeneratorByGrid(master=None):
	win = Tkinter.LabelFrame(master, text='Registration', height=400, width=500)
 	win.grid_propagate(False)
 	win.grid()

 	MyLabel = partial(Tkinter.Label, win, height=1, width=10)
 	MyText = partial(Tkinter.Text, win, height=1, width=20)
 	MyCombox = partial(ttk.Combobox, win, height=1, width=23)
 	MyButton = partial(Tkinter.Button, win, width=10)

 	for key in WIDGETS_DICT:
 		value = WIDGETS_DICT[key]
 		label = partial(MyLabel, text=value[0].decode('gbk').encode('utf-8'))
 		label().grid(row=value[2][0],column=value[2][1],sticky=Tkinter.W)

 		if value[1] == 'text':
 			text = partial(MyText)
 			text().grid(row=value[3][0],column=value[3][1],sticky=Tkinter.W)
 		elif value[1] == 'combobox':
 			if key == 'IDCard Type':
 				var = ['身份证','军官证']
 			elif key == 'Gender':
 				var = ['男','女']
 			elif key == 'Cost':
 				var = [1,10,0]
 			elif key == 'Status':
 				var = ['Draft','Confirm','Cancel']
 			elif key == 'Reg Type':
 				var = ['Clinic','Emergency']
 			elif key == 'Specialty':
 				var = ['Physical','Surgeon']
 			elif key == 'Doctor':
 				var = ['Johnson','Jimmy','Tony']
 			elif key == 'Insurance Type':
 				var = ['Free','TotalPay']
 			combo = partial(MyCombox)
 			combo(value=var,justify='center').grid(row=value[3][0],column=value[3][1],sticky=Tkinter.W)

 	regBtn = partial(MyButton, command=register, text='确 认'.decode('gbk').encode('utf-8'))
 	regBtn().grid(row=7,column=1)
 	cancelBtn = partial(MyButton, command=win.quit, text='取 消'.decode('gbk').encode('utf-8'))
 	cancelBtn().grid(row=7,column=3,sticky=Tkinter.W)

 


if __name__ == '__main__':
	top = Tkinter.Tk()
	top.title('挂号界面'.decode('gbk').encode('utf-8'))
	top.geometry('500x230')
	guiGeneratorByGrid(top)
	top.mainloop()



