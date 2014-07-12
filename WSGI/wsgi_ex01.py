#coding:utf-8
# This is a simplistic sample that a WSGI web server would like 

import StringIO
import sys

def run_wsgi_app(app, environ):
	body = StringIO.StringIO()

	def status_response(status, headers):
		body.write('Status:%s\r\n' % status)
		for header in headers:
			body.write('%s:%s\r\n' % header)
		return body

	iterable = app(environ, status_response)

	try:
		# StringIO.getvalue() 
		# 		Retrieve the entire contents of the “file” at any time before 
		if not body.getValue():
			raise RuntimeError('Status not write to reponse')
		body.write('\r\n%s\r\n' % '\r\n'.join(line for line in iterable))
	except Exception, e:
		raise e
	finally:
		# callable(object) 
		# 		Return True if the object argument appears callable, False if not.
		if hasattr(iterable, close) and callable(iterable.close):
			iterable.close()

	sys.stdout.write(body.getValue())
	sys.stdout.flush()
