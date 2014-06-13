#coding:utf-8

import sys,logging
import wsgilog


class Log(wsgilog.WsgiLog):
	def __init__(self, application,cfg=None):
		wsgilog.WsgiLog.__init__(
				self,
				application,
				logformat = '%(message)s',
				tofile = True,
				toprint = True,
				file = 'wsgilog.log',
				# file = cfg.log_file,
				# interval = config.log_interval,
				# backups = config.log_backups
			)

		# wsgilog 没有 LogIO
		# sys.stdout = wsgilog.LogIO(self.logger, logging.INFO)
		# sys.stderr = wsgilog.LogIO(self.logger, logging.ERROR)
