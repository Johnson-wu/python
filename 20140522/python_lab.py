# -*- coding: utf-8 -*-
# Python 3.3.3
# PyQt 5.1.1
import sys,time,re,urllib.parse,urllib.request,http.cookiejar,json
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

# """cookie"""
cookie=http.cookiejar.LWPCookieJar()
#cookie.load('f:/cookie.txt',True,True)
chandle=urllib.request.HTTPCookieProcessor(cookie)

# """获取数据"""
def getData(url):
    r=urllib.request.Request(url)
    opener=urllib.request.build_opener(chandle)
    u=opener.open(r)
    #chandle.cookiejar.save('f:/cookie.txt',True,True)
    data=u.read()
    try:
        data=data.decode('utf-8')
    except:
        data=data.decode('gbk','ignore')
    return data
def postData(url,data):
    data=urllib.parse.urlencode(data);data=bytes(data,'utf-8')
    r=urllib.request.Request(url,data)
    opener=urllib.request.build_opener(chandle)
    u=opener.open(r)
    #chandle.cookiejar.save('f:/cookie.txt',True,True)
    data=u.read()
    try:
        data=data.decode('utf-8')
    except:
        data=data.decode('gbk','ignore')
    return data
# """火车票"""
class Ticket:
    def init(self,s,e,d):
        self.li=[]
        cont=getData('https://kyfw.12306.cn/otn/resources/js/framework/station_name.js')
        s=re.findall('%s\|([^|]+)' % s,cont)[0]
        e=re.findall('%s\|([^|]+)' % e,cont)[0]
        url='https://kyfw.12306.cn/otn/lcxxcx/query?purpose_codes=0X00&queryDate=%s&from_station=%s&to_station=%s' % (d,s,e)
        cont=json.loads(getData(url))["data"]["datas"]
        name=[
            "station_train_code",
            "from_station_name",
            "to_station_name",
            "lishi",
            "swz_num",
            "tz_num",
            "zy_num",
            "ze_num",
            "gr_num",
            "rw_num",
            "yw_num",
            "rz_num",
            "yz_num",
            "wz_num",
            "qt_num"
        ]
        for x in cont:
            tmp=[]
            for y in name:
                if y=="from_station_name":
                    s=x[y]+'\n'+x["start_time"]
                    tmp.append(s)
                elif y=="to_station_name":
                    s=x[y]+'\n'+x["arrive_time"]
                    tmp.append(s)
                else:
                    tmp.append(x[y])
            self.li.append(tmp)
# """ui"""
class Dialog(QDialog):
    ticket=Ticket()
    def __init__(self):
        super().__init__()
        self.resize(750,350)
        #布局管理器
        self.layout=[QVBoxLayout(self),QHBoxLayout()]
        self.layout[1].setContentsMargins(0,0,0,0)
        self.layout[1].setSpacing(0)
        self.layout[0].setContentsMargins(0,0,0,0)
        self.layout[0].setSpacing(0)
        self.layout[0].addLayout(self.layout[1])
        #按钮
        btn=QPushButton("ok")
        btn.clicked.connect(self.submit)
        #输入选项
        label=[QLabel("发站:"),QLabel("到站:"),QLabel("日期:")]
        self.line=[QLineEdit(),QLineEdit(),QComboBox()]
        y=int(time.strftime("%Y",time.localtime()))
        m=int(time.strftime("%m",time.localtime()))
        d=int(time.strftime("%d",time.localtime()))
        i=0
        yy=y
        mm=m
        dd=d
        while i<20:
            if m in (1,3,5,7,8,10,12):
                if d+i>31:
                    dd=d+i-31
                    mm=m+1
                    if mm>12:
                        yy=y+1
                        mm=mm-12
                else:
                    dd=d+i
            elif m in (4,6,9,11):
                if d+i>30:
                    dd=d+i-30
                    mm=m+1
                    if mm>12:
                        yy=y+1
                        mm=mm-12
                else:
                    dd=d+i
            else:
                if (m%400==0) or ((m%4==0) and (m%100!=0)):
                    if d+i>29:
                        dd=d+i-29
                        mm=m+1
                        if mm>12:
                            yy=y+1
                            mm=mm-12
                    else:
                        dd=d+i
                else:
                    if d+i>28:
                        dd=d+i-28
                        mm=m+1
                        if mm>12:
                            yy=y+1
                            mm=mm-12
                    else:
                        dd=d+i
            s='%d-%02d-%02d' % (yy,mm,dd)
            self.line[2].addItem(s)
            i+=1
        i=0
        while i<3:
            self.line[i].setMaximumWidth(100)
            label[i].setMaximumWidth(50)
            label[i].setAlignment(Qt.AlignRight|Qt.AlignVCenter)
            self.layout[1].addWidget(label[i],Qt.AlignRight)
            self.layout[1].addWidget(self.line[i],Qt.AlignLeft)
            i+=1
        self.layout[1].addWidget(btn)
        #表格
        head=['车次','发站','到站','历时','商务座','特等座','一等座','二等座','高级软卧','软卧','硬卧','软座','硬座','无座','其他']
        self.table=QTableWidget()
        self.table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.table.setColumnCount(15)
        self.table.setHorizontalHeaderLabels(head)
        self.layout[0].addWidget(self.table)
        self.show()
    def submit(self):
        self.table.clearContents()
        s=self.line[0].text()
        e=self.line[1].text()
        d=self.line[2].currentText()
        self.ticket.init(s,e,d)
        self.table.setRowCount(len(self.ticket.li))
        i=0
        for x in self.ticket.li:
            j=0
            for y in x:
                if j==1 or j==2:
                    item=QLabel(y)
                    item.setAlignment(Qt.AlignCenter)
                    self.table.setCellWidget(i,j,item)
                else:
                    item=QTableWidgetItem(y)
                    item.setTextAlignment(Qt.AlignCenter)
                    if not re.search('\D',y):
                        item.setForeground(QBrush(Qt.red))
                    self.table.setItem(i,j,item)
                if j>2 or j==0:
                    self.table.resizeColumnToContents(j)
                j+=1
            i+=1
if __name__=="__main__":
    app=QApplication(sys.argv)
    dialog=Dialog()
    sys.exit(app.exec_())