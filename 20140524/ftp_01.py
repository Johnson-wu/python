#coding:utf-8

import ftplib

HOST = 'ftp.mozilla.org'
DIRECTORY = 'pub/mozilla.org/webtools'
FILENAME = 'bugzilla-4.0-to-4.0.10.diff.gz'

def main():
	try:
		ftp = ftplib.FTP(HOST)
	except (socket.error, socket.gaierror) as e:
		print('Failed to connect')
		raise e
	print('Success to connect ', HOST)

	try:
		ftp.login()
	except ftplib.error_perm as e:
		print('Failed to login')
		raise e
	print('Success to login in ')

	try:
		ftp.cwd(DIRECTORY)
	except Exception as e:
		print('Failed to cd')
		raise e
	print('Sucess to cd directory ')

	try:
		ftp.retrlines('LIST')
	except Exception as e:
		print('Failed to List directory %s' % DIRECTORY)
		raise e
	print('Sucess to list directory %s' % DIRECTORY)

	try:
		# FTP.retrbinary(cmd, callback, blocksize=8192, rest=None) 
		# 	Retrieve a file in binary transfer mode. cmd should be an appropriate RETR command: 'RETR filename'. 
		# 	The callback function is called for each block of data received, with a single string argument giving the data block. 
		# 	The optional blocksize argument specifies the maximum chunk size to read on the low-level socket object 
		# 	created to do the actual transfer (which will also be the largest size of the data blocks passed to callback). 
		# 	A reasonable default is chosen. rest means the same thing as in the transfercmd() method.
		ftp.retrbinary('RETR %s' % FILENAME, open(FILENAME,'wb').write)
	except Exception as e:
		print('Failed to download')
		raise e
	print('Sucess to download %s' % FILENAME)

	ftp.quit()



if __name__ == '__main__':
	main()
	
