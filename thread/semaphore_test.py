#coding:utf-8

import multiprocessing
import time 

def worker(s,i):
    s.acquire()
    print(multiprocessing.current_process().name + " acquire")
    time.sleep(i)
    print(multiprocessing.current_process().name + " release")
    s.release()

if __name__ == "__main__":
  	# 信号值是3，不是应该可以同时有三个进程可以访问资源吗？怎么还是同时只有一个进程Acquire?
    s = multiprocessing.Semaphore(2)
    for i in range(5):
        multiprocessing.Process(target=worker, args=(s,5)).start()
        