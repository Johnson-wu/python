# -*- coding:utf-8 -*-

# Python����: windowsƽ̨�������Pythonɱ����
#from : http://www.joyloft.net/?p=1031
# "��δ���������һ���ܼ򵥵ĳ�����
#  ��python�е�һ�����򡣸������������һ��timeout
#  ����һ��ʱ�����û�з��أ���ɱ���������¿��Ľ��̡�
#  ������Ϊ�ҿ϶����ǵ�һ���������������ˣ�
#  �����������˺þö�û�ҵ������İ취���Լ�����һ����"

#��������ctypes�ķ���û�гɹ��������б�Ҳ�������������õ�ɱ���̵�winprocҲ��֪����ʲô�����϶�û�в鵽
# ���ǽ�������ķ�������ɱ������
# import os 
 
# command = "taskkill /F /IM ������.exe"    # ���߰ѽ���������PID��Ҳ��
# os.system(command)


# ctypes��python��һ���ⲿ�⣬�ṩ��C���Լ��ݵ��������ͣ����Ժܷ���ص���C����ľ�̬��Ͷ�̬���еĺ���
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
		# print >> sys.stderr, "Failed getting first process." #???python2�����������
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