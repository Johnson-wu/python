#coding:utf-8

# 使用pipe进行进程间的通信。pipe有两种类型，一种单向，一种双向（duplex)
# 有几个疑问：
# 一、进入pipe的消息是按什么顺序取出的？是按先进先出的原则
# 二、为何下面proc1()中的打印当前进程pid的顺序反而在proc2打印recv之后？
# 三、proc1里的打印顺序很奇怪！

import multiprocessing as multiproc
import time,os

def proc1(pipe):
	print(multiproc.current_process().pid)
	print(os.getpid())	# 和上面方法一样，可以获得当前进程的pid
	pipe.send([('Hello , my name is process %s !' % multiproc.current_process().pid), multiproc.current_process().pid])
	pipe.send([('This is process %s second send !' % multiproc.current_process().pid), multiproc.current_process().pid])
	print('waiting....')
	print(pipe.recv())

def proc2(pipe):
	time.sleep(3)	# 根据加了等待的效果来看，pipe中一端发了消息之后，进程会被阻塞，等待pipe另一端来取走消息
	receive = pipe.recv()
	# print(pipe.recv())
	print(receive)
	print(pipe.recv())
	pipe.send('Nice to meet you process %s. I\'m process %s.' % (receive[1], multiproc.current_process().pid))
	# print(pipe.recv())

# 获取一个管道，默认是双向的。每个管道有两个端口（即两个connection)
pipe = multiproc.Pipe()

# 创建进程的时候一定要是主程序才可以，为何？
if __name__ == '__main__':
	process1 = multiproc.Process(target=proc1,args=(pipe[0],)) # 取出第一个connection，传递给进程
	process2 = multiproc.Process(target=proc2,args=(pipe[1],)) # 取出第二个connection，传递给进程
	# process3 = multiproc.Process(target=proc1,args=(pipe[0],)) # 取出第二个connection，传递给进程


	process1.start()
	process2.start()
	# process3.start()

	process1.join()
	process2.join()
	# process3.join()

	print('Main process is %s ' % multiproc.current_process().pid)