#!/usr/bin/python
# -*- coding: utf-8 -*-
""" download - slave
"""
__author__ = 'Zagfai'
__license__ = 'MIT@2014-02'
  
import webtul
from multiprocessing.connection import Client
  
a = 0
try:
    while True:
        a += 1
        address = ('10.33.41.112', 6666)
        conn = Client(address, authkey='hellokey')
        #print conn.recv()
        d = conn.recv()
        conn.close()
except:
    pass
print a