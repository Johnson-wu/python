# -*- coding=utf-8 -*-
import os
import sys
import chardet
reload(sys);
sys.setdefaultencoding('utf-8');

for dirpath, dirnames, filenames in os.walk(r'E:\\GitHub\\python'):
    print 'Directory', dirpath
    afff=dirnames
    typeEncode = sys.getfilesystemencoding()
    a=u'我的编码是:'
    print a.encode('gbk'),chardet.detect(str(afff))
    fafa=chardet.detect(str(afff))['encoding']
    print 'dirnames',str(afff).decode(fafa,"ignore").encode(typeEncode)
    for filename in filenames:
        print ' File', filename