#coding:utf-8

import Tkinter 
import ttk
from functools import partial

WIDGETS_DICT = {
	'IDCard Type': ['证件类型:','combobox',(0,0),(0,1),'cardInfo'],
	'IDCard Number': ['证件号码:','text',(0,2),(0,3),'cardInfo'],
	'Name': ['姓   名 :','text',(0,0),(0,1),'basicInfo'],
	'PinYin': ['首   拼 :','text',(0,2),(0,3),'basicInfo'],
	'Gender': ['性   别 :','combobox',(1,0),(1,1),'basicInfo'],
	'Brithday': ['出生日期:','text',(1,2),(1,3),'basicInfo'],
	'Address': ['地   址 :','text',(2,0),(2,1),'basicInfo'],
	'Phone': ['联系方式:','text',(2,2),(2,3),'basicInfo'],
	'Status': ['状   态 :','combobox',(0,0),(0,1),'medInfo'],
	'Cost': ['挂号收费:','combobox',(0,2),(0,3),'medInfo'],
	'Reg Type': ['挂号类型 :','combobox',(1,0),(1,1),'medInfo'],
	'Specialty': ['挂号科室 :','combobox',(1,2),(1,3),'medInfo'],
	'Doctor': ['医   生 :','combobox',(2,0),(2,1),'medInfo'],
	'Insurance Type': ['医保类型:','combobox',(2,2),(2,3),'medInfo']
}


def register():
	pass

def guiGeneratorByGrid(master=None):
	cardInfo = Tkinter.LabelFrame(master, text='Card Info', height=50, width=500)
	basicInfo = Tkinter.LabelFrame(master, text='Basic Info', height=100, width=500)
	medInfo = Tkinter.LabelFrame(master, text='Med Info', height=100, width=500)
	btnFrame = Tkinter.Frame(master,height=50,width=500)

	frames = [cardInfo,basicInfo,medInfo,btnFrame]
	for win in frames:
	 	win.grid_propagate(False)
	 	win.grid()

 	MyLabel = partial(Tkinter.Label, height=1, width=10)
 	MyText = partial(Tkinter.Text, height=1, width=20)
 	MyCombox = partial(ttk.Combobox, height=1, width=23)
 	MyButton = partial(Tkinter.Button, btnFrame, width=10)

 	for key in WIDGETS_DICT:
 		value = WIDGETS_DICT[key]
 		if value[4] == 'cardInfo':
 			parent = cardInfo
 		elif value[4] == 'basicInfo':
 			parent = basicInfo
 		else:
 			parent = medInfo
 		label = partial(MyLabel, parent, text=value[0].decode('gbk').encode('utf-8'))
 		label().grid(row=value[2][0],column=value[2][1],sticky=Tkinter.W)
  
 		if value[1] == 'text':
 			text = partial(MyText, parent)
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
 			combo = partial(MyCombox, parent)
 			combo(value=var).grid(row=value[3][0],column=value[3][1],sticky=Tkinter.W)

 	layLabel1 = partial(MyLabel,btnFrame,width=18)
 	layLabel2 = partial(MyLabel,btnFrame,width=15)
 	layLabel1().grid(row=0,column=0)
 	layLabel2().grid(row=0,column=2)
 	regBtn = partial(MyButton, command=register, text='确  定'.decode('gbk').encode('utf-8'))
 	regBtn().grid(row=0,column=1)
 	cancelBtn = partial(MyButton, command=win.quit, text='取  消'.decode('gbk').encode('utf-8'))
 	cancelBtn().grid(row=0,column=3)

 


if __name__ == '__main__':
	top = Tkinter.Tk()
	top.title('挂号界面'.decode('gbk').encode('utf-8'))
	top.geometry('550x300')
	# top['justify'] = 'center'
	guiGeneratorByGrid(top)
	top.mainloop()



