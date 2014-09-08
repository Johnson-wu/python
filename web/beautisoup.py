import urllib2
import os  
from BeautifulSoup import *
import re  
siteUrls = " "  
  
url = "http://www.sina.com.cn"  
def getContent(url):  
    content = urllib2.urlopen(url).read()  
    content = writeCss(url,content)  
    content = writefileName(url,content)  
    fileNames = re.findall(r'/[^\?]*\?([^/|^\?]*)$',url)  
    fileName = fileNames[0]  
    print fileName  
    f = file(fileName+".html",'w')  
    f.write(content)  
    f.close()  
  
def writeCss(url,content):  
    soup = BeautifulSoup(content)  
    csss = soup.findAll('link',attrs={'type':'text/css'})  
    css_pat = re.compile('.*/(.*)\.css')  
    fileNames = re.findall(r'/[^\?]*\?([^/|^\?]*)$',url)
    print fileNames
    fileName = fileNames[0]  
    print fileName  
    for css in csss:  
        cssnames = re.findall(r'.*/(.*)\.css',str(css))  
        cssurls = re.findall(r'.*href=\"([^\"]*)\"',str(css))  
#       print cssnames[0]  
#       print cssurls[0]  
        cssurl = "http://review.artintern.net/" + cssurls[0]  
#       print cssurl  
        content = content.replace(cssurls[0],fileName + "/" + cssnames[0]+".css")  
        print os.path.isdir(fileName)  
        if not os.path.isdir(fileName):  
            os.mkdir(fileName)  
        csscontent = urllib2.urlopen(cssurl).read()  
        cssNewName = fileName+"/"+cssnames[0]+".css"  
        cssfile = file(cssNewName,'w')  
        cssfile.write(csscontent)  
        cssfile.close()  
    return content  
  
def writefileName(url,content):  
    soup = BeautifulSoup(content)  
    imgs = soup.findAll('img')  
    img_pat = re.compile('.*/(.*)\.[jpg|gif]')  
    fileNames = re.findall(r'/[^\?]*\?([^/|^\?]*)$',url)  
    fileName = fileNames[0]  
    for img in imgs:  
        imgNames = re.findall(r'.*/(.*)\.[jpg|gif]',str(img))  
        imgType = re.findall(r'.*/.*\.([^ ]*)"',str(img))  
        imgUrls = re.findall(r'.*src=\"([^\"]*)\"',str(img))  
#       print imgNames[0]  
#       print imgType[0]  
#       print imgUrls[0]  
        imgUrl = "http://review.artintern.net/" + imgUrls[0]  
#       print imgUrl  
        content = content.replace(imgUrls[0],fileName+"/"+imgNames[0]+"."+imgType[0])  
        if not os.path.isdir(fileName):  
            os.mkdir(fileName)  
        imgContent = urllib2.urlopen(imgUrl).read()  
        imgNewName = fileName+"/"+imgNames[0]+"."+imgType[0]  
        imgfile = file(imgNewName,'w')  
        imgfile.write(imgContent)  
        imgfile.close()  
    return content  
  
getContent(url)  