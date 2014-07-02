#coding:utf-8

import Tkinter 
import ttk
from functools import partial

WIDGETS_DICT = {
	'IDCard Type': ['֤������:','combobox',(0,0),(0,1)],
	'IDCard Number': ['֤������:','text',(0,2),(0,3)],
	'Name': ['��  �� :','text',(1,0),(1,1)],
	'PinYin': ['��  ƴ :','text',(1,2),(1,3)],
	'Gender': ['��  �� :','combobox',(2,0),(2,1)],
	'Brithday': ['��������:','text',(2,2),(2,3)],
	'Address': ['��  ַ :','text',(3,0),(3,1)],
	'Phone': ['��ϵ��ʽ:','text',(3,2),(3,3)],
	'Status': ['״  ̬ :','combobox',(4,0),(4,1)],
	'Cost': ['�Һŷ�:','combobox',(4,2),(4,3)],
	'Reg Type': ['��  �� :','combobox',(5,0),(5,1)],
	'Specialty': ['��  �� :','combobox',(5,2),(5,3)],
	'Doctor': ['ҽ  �� :','combobox',(6,0),(6,1)],
	'Insurance Type': ['ҽ������:','combobox',(6,2),(6,3)]
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
	cardType_lb().pack(side='top')	# ע��cardType_lb()�����()������ϣ���Ȼ����AttributeError: 'functools.partial' object has no attribute 'pack'
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
 				var = ['���֤','����֤']
 			elif key == 'Gender':
 				var = ['��','Ů']
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

 	regBtn = partial(MyButton, command=register, text='ȷ ��'.decode('gbk').encode('utf-8'))
 	regBtn().grid(row=7,column=1)
 	cancelBtn = partial(MyButton, command=win.quit, text='ȡ ��'.decode('gbk').encode('utf-8'))
 	cancelBtn().grid(row=7,column=3,sticky=Tkinter.W)

 


if __name__ == '__main__':
	top = Tkinter.Tk()
	top.title('�ҺŽ���'.decode('gbk').encode('utf-8'))
	top.geometry('500x230')
	guiGeneratorByGrid(top)
	top.mainloop()



