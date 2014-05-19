#coding:utf-8
# 通过使用subprocess包，我们可以运行外部程序。这极大的拓展了Python的功能。
import subprocess

# 使用shell来解释前面的一个字符串参数
sub = subprocess.call('dir',shell=True) 

# 这种写法，是变命令名与参数分开，组合成一个列表传递给subprocess
sub2 = subprocess.call(['ping','localhost']) 
# subprocess.call调用子进程后，父进程会被block，直到子进程结束
print('Main process.')

# 通过Popen调用子进程，父进程不会等待子进程结束，而是同时进行
sub3 = subprocess.Popen(['ping','localhost'])
print('Main process invoke sub3 by Popen')


sub4 = subprocess.Popen(['ping','localhost'])
sub4.wait()	# 子进程调用wait()后，会阻塞父进程，直到子进程结束之后，父进程继续
print('Main process invoke sub4 by Popen')

