# -*- coding:utf-8 -*-

# Python语言: windows平台下如何用Python杀进程
#from : http://www.joyloft.net/?p=1031
# "这段代码来自于一个很简单的场景：
#  在python中调一个程序。给这个程序设置一个timeout
#  假如一段时间程序还没有返回，就杀掉这个这个新开的进程。
#  本来以为我肯定不是第一个遇到这个问题的人，
#  但是网上搜了好久都没找到完整的办法，自己搞了一个。"

#下面利用ctypes的方法没有成功，进程列表也读不出来，调用的杀进程的winproc也不知道是什么，网上都没有查到
# 但是紧接着面的方法可以杀掉进程
# import os 
 
# command = "taskkill /F /IM 进程名.exe"    # 或者把进程名换进PID号也行
# os.system(command)


# ctypes是python的一个外部库，提供和C语言兼容的数据类型，可以很方便地调用C编译的静态库和动态库中的函数
from ctypes import *
import sys

TH32CS_SNAPPROCESS = 0x00000002

class processentry32(Structure):
	_fields_ = [
		("dwSize", c_ulong),
        ("cntUsage", c_ulong),
        ("th32ProcessID", c_ulong),
        ("th32DefaultHeapID", c_ulong),
        ("th32ModuleID", c_ulong),
        ("cntThreads", c_ulong),
        ("th32ParentProcessID", c_ulong),
        ("pcPriClassBase", c_ulong),
        ("dwFlags", c_ulong),
        ("szExeFile", c_char * 260)	
	]
	
	
def getProcList():
	CreateToolhelp32Snapshot = windll.kernel32.CreateToolhelp32Snapshot
	Process32First = windll.kernel32.Process32First
	Process32Next = windll.kernel32.Process32Next
	CloseHandle = windll.kernel32.CloseHandle
	hProcessSnap = CreateToolhelp32Snapshot(TH32CS_SNAPPROCESS,0)
	pe32 = processentry32()
	pe32.dwSize = sizeof(processentry32)
	
	if Process32First(hProcessSnap, byref(pe32)) == False:
		# print >> sys.stderr, "Failed getting first process." #???python2有这种输出吗？
		print(sys.stderr, " Failed getting first process.")
		return
	
	while True:
		yield pe32 # ???
		if Process32Next(hProcessSnap, byref(pe32)) == False:
			break
	
	CloseHandle(hProcessSnap)
	
	
def getChildPid(pid):
	procList = getProcList()
	for proc in procList:
		if proc.th32ParentProcessID == pid:
			yield proc.th32ProcessID


def killPid(pid):
	childList = getChildPid(pid)
	for childPid in childList:
		killPid(childPid)
	handle = windll.kernel32.OpenProcess(1, False, pid)
	windll.kernel32.TerminateProcess(handle,0)
	

if __name__ == '__main__':  
    procList = getProcList()  
    for proc in procList:  
        print("proc.szExeFile=%s, proc.th32ParentProcessID=%d, proc.th32ProcessID=%d" % (proc.szExeFile, proc.th32ParentProcessID, proc.th32ProcessID)) 
	
# Test1
# if __name__ == "__main__":
	# args = sys.argv
	# print(args)
	# if len(args) > 1:
		# pid = int(args[1])
		# print(pid)
		# killPid(pid)
	# else:
		# procList = getProcList()
		# for proc in procList:
			# print(proc.szExeFile + '  ' + str(proc.th32ParentProcessID) + '  ' + str(proc.th32ProcessID))
			
			
# Test2	
# import subprocess
# import time
# # import winproc

# timeout = 2
# process = subprocess.Popen("cmd /k ping localhost -t", shell=True)
# start = int(time.time())

# while process.poll() == None:
	# now = int(time.time())
	# print(process.pid)
	# if int(now - start) > timeout:
		# pid = process.pid
		# print("Timeout Pid is : ",pid)
		# break
	
# # winproc.killPid(pid)

# print("End !")