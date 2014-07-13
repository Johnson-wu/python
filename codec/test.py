# -*- coding=utf-8 -*-
import os
import sys
import chardet
reload(sys);
sys.setdefaultencoding('utf-8');

for dirpath, dirnames, filenames in os.walk('E:\\test'):
    print 'Directory', dirpath
    afff=dirnames
    typeEncode = sys.getfilesystemencoding()
    a=u'我的编码是:'
    print a.encode('gbk'),chardet.detect(str(afff))
    fafa=chardet.detect(str(afff))['encoding']
    print 'fafa',fafa
    for name in afff:
    	print 'dirname',name,chardet.detect(name)
#     # for filename in filenames:
#     #     print ' File', filename

print '======================================'
s = '\xd0\xc2\xbd\xa8\xce\xc4\xbc\xfe\xbc\xd0 - \xb8\xb1\xb1\xbe'
print s.decode(chardet.detect(s)['encoding']).encode('gbk'),chardet.detect(s)['encoding']