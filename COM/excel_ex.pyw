#coding:utf-8

from Tkinter import Tk
from time import sleep
from tkMessageBox import showwarning
import win32com.client as win32


warn = lambda app: showwarning(app, 'Exit?')
RNAGE = range(3,8)

def excel():
	# start the Excel
	app = 'Excel'
	xl = win32.gencache.EnsureDispatch('%s.Application' % app)
	# add a workbook(a spreadsheet that contains sheets)
	ss = xl.Workbooks.Add()
	# grab a handle to the active sheet
	sh = ss.ActiveSheet
	# excel app whether visible
	xl.Visible = True
	sleep(1)

	sh.Cells(1,1).Value = 'Python-to-%s Demo' % app
	sleep(1)
	for i in RNAGE:
		sh.Cells(i,1).Value = 'Line %d' % i
		sleep(1)
	# varible i is also valid out of loops. This's very different from java
	sh.Cells(i+2,1).Value = 'Th-th-th-that\'s all folks!'
	# Tk dialog
	warn(app)
	# Exit excel without saving
	ss.Close(False)
	xl.Application.Quit()


if __name__ == '__main__':
	Tk().withdraw()
	excel()