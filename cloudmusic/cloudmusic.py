#coding:utf-8

import os
import copy
import time

SOURCE_DIR = 'E:\\CloudMusic'
DES_DIR = 'E:\\music_total'
COUNT = 0

def copyMusic(sourceDir, desDir):
	global COUNT
	if os.path.exists(sourceDir):
		for f in os.listdir(sourceDir):
			absolute_path = os.path.join(sourceDir,f)
			if os.path.isdir(absolute_path):
				copyMusic(absolute_path,desDir)
			else:
				# print absolute_path
				# print os.path.join(desDir,f)
				COUNT += 1
				result = os.system('copy "%s" "%s"' % (absolute_path,os.path.join(desDir,f)))
				# print result

def _main():
	copyMusic(SOURCE_DIR,DES_DIR)
	print 'Total copy : %d' % COUNT



if __name__ == '__main__':
	print 'Begin to copy mp3 at %s' % time.ctime()
	_main()
	print 'Copy mp3 finished at %s' % time.ctime()

