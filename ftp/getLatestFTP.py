#coding:utf-8

from ftplib import *
import os 
import socket

HOST = 'ftp.mozilla.org'
DIR = 'pub/mozilla.org/webtools'
FILE = 'bugzilla-LATEST.tar.gz'

def main():
	try:
		# Ftp's low-level still use socket. But it will create a pair of socket, 
		# one is for cmd control, one is for data transfer.
		f = FTP(HOST)
	except (socket.error, socket.gaierror) as e:
		print 'ERROR: %s . Couldn\'t connect to %s' % (e,HOST)
		return
	print 'connected to %s' % HOST

	try:
		f.login()
	except Exception, e:
		print 'ERROR: %s . Couldn\'t login to %s' % (e,HOST)
		return
	print 'Successfully login to %s' % HOST

	try:
		f.cwd(DIR)
	except Exception, e:
		print 'ERROR: %s . Couldn\'t change directory to %s' % (e,DIR)
		return
	print 'Successfully go into directory %s' % DIR

	try:
		# FTP.retrbinary(command, callback[, maxblocksize[, rest]]) 
		# Retrieve a file in binary transfer mode. command should be an appropriate RETR command: 'RETR filename'. 
		# The callback function is called for each block of data received, with a single string argument giving the data block.
		# The optional maxblocksize argument specifies the maximum chunk size to read on the low-level socket object created to \
		# do the actual transfer (which will also be the largest size of the data blocks passed to callback). 
		# A reasonable default is chosen. rest means the same thing as in the transfercmd() method
		f.retrbinary('RETR %s' % FILE, open(FILE,'a').write)
	except Exception, e:
		print 'ERROR: %s . Couldn\'t download %s' % (e,FILE)
		os.unlink(FILE)		# the same to function remove()
		return
	print 'Successfully download file %s' % FILE

	f.quit()




if __name__ == '__main__':
	main()


