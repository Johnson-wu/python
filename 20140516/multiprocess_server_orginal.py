#!/usr/bin/python
# -*- coding: utf-8 -*-
""" downloader - master server
"""
__author__ = 'Zagfai'
__license__ = 'MIT@2014-02'
  
import webtul
from multiprocessing.connection import Listener
from threading import Thread
  
def listener():
    address = ('10.33.41.112', 6666)
    listener = Listener(address, backlog=100, authkey='hellokey')
    while True:
        conn = listener.accept()
        #print 'connection accepted from', listener.last_accepted
        try:
            conn.send({'1':2, '2':'abc'})
        except Exception, e:
            print e
        finally:
            conn.close()
    listener.close()
  
listener_th = Thread(target=listener)
listener_th.daemon = True
listener_th.start()
listener_th.join(timeout=100)