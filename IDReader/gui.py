#coding:utf-8

import Tkinter 
import ttk
from functools import partial

WIDGETS_DICT = {
	'IDCard Type': ['֤������:','combobox',(0,0),(0,1),'cardInfo'],
	'IDCard Number': ['֤������:','text',(0,2),(0,3),'cardInfo'],
	'Name': ['��   �� :','text',(0,0),(0,1),'basicInfo'],
	'PinYin': ['��   ƴ :','text',(0,2),(0,3),'basicInfo'],
	'Gender': ['��   �� :','combobox',(1,0),(1,1),'basicInfo'],
	'Brithday': ['��������:','text',(1,2),(1,3),'basicInfo'],
	'Address': ['��   ַ :','text',(2,0),(2,1),'basicInfo'],
	'Phone': ['��ϵ��ʽ:','text',(2,2),(2,3),'basicInfo'],
	'Status': ['״   ̬ :','combobox',(0,0),(0,1),'medInfo'],
	'Cost': ['�Һ��շ�:','combobox',(0,2),(0,3),'medInfo'],
	'Reg Type': ['�Һ����� :','combobox',(1,0),(1,1),'medInfo'],
	'Specialty': ['�Һſ��� :','combobox',(1,2),(1,3),'medInfo'],
	'Doctor': ['ҽ   �� :','combobox',(2,0),(2,1),'medInfo'],
	'Insurance Type': ['ҽ������:','combobox',(2,2),(2,3),'medInfo']
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
 			combo = partial(MyCombox, parent)
 			combo(value=var).grid(row=value[3][0],column=value[3][1],sticky=Tkinter.W)

 	layLabel1 = partial(MyLabel,btnFrame,width=18)
 	layLabel2 = partial(MyLabel,btnFrame,width=15)
 	layLabel1().grid(row=0,column=0)
 	layLabel2().grid(row=0,column=2)
 	regBtn = partial(MyButton, command=register, text='ȷ  ��'.decode('gbk').encode('utf-8'))
 	regBtn().grid(row=0,column=1)
 	cancelBtn = partial(MyButton, command=win.quit, text='ȡ  ��'.decode('gbk').encode('utf-8'))
 	cancelBtn().grid(row=0,column=3)

 


if __name__ == '__main__':
	top = Tkinter.Tk()
	top.title('�ҺŽ���'.decode('gbk').encode('utf-8'))
	top.geometry('550x300')
	# top['justify'] = 'center'
	guiGeneratorByGrid(top)
	top.mainloop()



