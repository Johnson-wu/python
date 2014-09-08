#coding:utf-8

import cStringIO
import formatter
from htmllib import HTMLParser
import httplib
import os
import sys
import urllib
import urlparse

from BeautifulSoup import BeautifulSoup
import chardet

class Retriever(object):
    __slots__ = ('url','file','links')

    def __init__(self, url):
        self.url, self.file = self.get_file(url)
        self.links = []

    # 解析url在本地文件系统中创建相应的目录
    def get_file(self, url, default='index.html'):
        parsed = urlparse.urlparse(url)
        host = parsed.netloc.split('@')[-1].split(':')[0]
        # print parsed
        filepath = '%s%s' % (host, parsed.path)

        if not os.path.splitext(parsed.path)[1]:
            filepath = os.path.join(filepath, default)
        linkdir = os.path.dirname(filepath)
        # print filepath, linkdir
        if not os.path.isdir(linkdir):  
            os.makedirs(linkdir)
        return url, filepath

    def download(self):
        try:
            if os.path.exists(self.file):
                # print self.file
                return (self.url, self.file)
            # urllib.urlretrieve(url[, filename[, reporthook[, data]]]) 
            #       Copy a network object denoted by a URL to a local file, if necessary.
            #       If the URL points to a local file, or a valid cached copy of the object exists, the object is not copied.
            #       Return a tuple (filename, headers) where filename is the local file name under which the object can be found, 
            #       and headers is whatever the info() method of the object returned by urlopen() returned (for a remote object, possibly cached). 
            retval = urllib.urlretrieve(self.url, self.file)
        except Exception, e:
            retval = (('*** Error: bad URL "%s": %s' % (self.url, e)),)
        # print 'retval: ', retval
        return retval

    # 将下载的url object复制到本地文件中
    def download2(self):
        # print '1 Prepare to download : ',self.file
        try:
            if os.path.exists(self.file):
                # print 'exists file : ',self.file
                return (self.url, self.file)
            if 'htm' in self.file or 'html' in self.file:
                # print 'Soup parse ...'
                data = self.parse_links_by_soup()
                pipe = open(self.file,'w')
                pipe.write(data)
                pipe.close()
                retval = (self.url, self.file)
            else:
                retval = urllib.urlretrieve(self.url, self.file)
        except Exception, e:
            retval = (('*** Error: bad URL "%s": %s' % (self.url, e)),)
        # print 'retval: ', retval
        return retval

    def parse_links_by_soup(self):
        print '2 begin to parse : ',self.url
        content = urllib.urlopen(self.url).read()
        # codec = chardet.detect(content)
        # print codec
        soup = BeautifulSoup(content)
        href_tags = soup.findAll(href=True)
        src_tags = soup.findAll(src=True)
        # print 'href' in a_tags[0]
        for tag in href_tags:
            # if tag['href'].startswith('/'):
            #     tag['href'] = tag['href'][1:]
            self.links.append(tag['href'])
        # src_tags[0]['src'] = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
        for tag in src_tags:
            # if tag['src'].startswith('/'):
            #     tag['src'] = tag['src'][1:]
            self.links.append(tag['src'])
        # print self.links
        return str(soup)
        

class Crawler(object):
    count = 0

    def __init__(self, url, logFile):
        # a queue of links that need to download
        self.q = [url]
        # all links that have been downloaded
        self.seen = set()  # 集合
        parsed = urlparse.urlparse(url)
        # print parsed
        host = parsed.netloc.split('@')[-1].split(':')[0]
        # print host
        self.dom = '.'.join(host.split('.')[-2:])
        # print self.dom
        self.logFile = logFile

    def get_page(self, url, media=False):
        # 先将符合要求的页面下载再进行解析
        r = Retriever(url)
        if 'www.artima.com' not in r.file:
            return  
        res = r.download()

        if '***' in res[0]:
            # print fname, '... skipping parse'
            self.logFile.write('Error : Download Failed --- %s \n' % res[0])
            return 
        # print "Download url : %s" % res[0]
        # print res[1]

        Crawler.count += 1
        self.seen.add(url)
        ftype = os.path.splitext(r.file)[1]
        # print ftype
        # 只下载html文件
        if ftype not in ('.htm','.html'):
            return
        
        r.parse_links_by_soup()
        links = r.links
        # print links
        for link in links:
            if link.startswith('mailto:'):
                # print '... discarded, mailto link'
                continue
            if not media:
                ftype = os.path.splitext(link)[1]
                if ftype in ('.mp3','.mp4','.m4v','.wav'):
                    # print '... discarded, media file'
                    continue
            if not link.startswith('http://'):
                # print '3 url---> %s , link---> %s' % (url,link)
                # self.logFile.write('3 url---> %s , link---> %s \n' % (url,link))
                link = urlparse.urljoin(url, link)
                # print link

            # print '*', link
            if link not in self.seen:
                if self.dom not in link:
                    pass
                    # print '... discarded, not in domain'
                else:
                    if link not in self.q:
                        if 'html' in link or 'htm' in link:
                            if 'pins1ed' in link and '#' not in link:
                                # 对于页面中符合要求的链接放入self.q列表中
                                self.q.append(link)
                                # print 'new pins1ed : %s, added to Q---len : %s' % (link,len(self.q))
                                self.logFile.write('HTML Url : %s === len : %s  \n' % (link,len(self.q)))
                        else:
                            self.q.append(link)
                            self.logFile.write('CSS/IMG Url : %s \n' % link)
                            pass
                    else:
                        pass
                        # print '... discarded, already in Q'
            else:
                pass
                # print '... discarded, already processed'

    def go(self, media=False):
        while self.q:
            url = self.q.pop()
            # print url
            self.get_page(url, media)
        self.logFile.write('Total Download : %s' % Crawler.count)
        self.logFile.close()


def _main():
    url = 'www.artima.com/pins1ed'
    if not url.startswith('http://') and \
        not url.startswith('ftp://'):
        url = 'http://%s/' % url 
    logFile = open(os.path.join(os.getcwd(),'crawler.log'),'w')
    robot = Crawler(url,logFile)
    robot.go()



if __name__ == '__main__':
    _main()

    # url = 'www.artima.com/pins1ed'
    # if not url.startswith('http://') and \
    #     not url.startswith('ftp://'):
    #     url = 'http://%s/' % url 
    # retre = Retriever(url)
    # data = retre.parse_links_by_soup()
    # print data

    # f = open('test.html','w')
    # f.write(data)
    # f.close()




