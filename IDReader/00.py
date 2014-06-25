#coding:utf-8

# print b'\xce\xe2\xbe\xa4'.decode('gb2312')

st = '\xce\xe2\xbe\xa4'

print st.decode('gbk').encode('utf-8')
# print st.decode('gbk').encode('gbk')



日志名称:          Application
来源:            Application Error
日期:            2014/6/25 14:56:04
事件 ID:         1000
任务类别:          (100)
级别:            错误
关键字:           经典
用户:            暂缺
计算机:           WIN-2GTCJVJJS1T
描述:
错误应用程序名称: python.exe，版本: 0.0.0.0，时间戳: 0x538b985c
错误模块名称: python27.dll，版本: 2.7.7150.1013，时间戳: 0x538b9859
异常代码: 0xc0000005
错误偏移量: 0x00031fe8
错误进程 ID: 0x1490
错误应用程序启动时间: 0x01cf9042863370b8
错误应用程序路径: C:\Python27\python.exe
错误模块路径: C:\Windows\system32\python27.dll
报告 ID: c5c1556d-fc35-11e3-b480-000c29e878b9
事件 Xml:
<Event xmlns="http://schemas.microsoft.com/win/2004/08/events/event">
  <System>
    <Provider Name="Application Error" />
    <EventID Qualifiers="0">1000</EventID>
    <Level>2</Level>
    <Task>100</Task>
    <Keywords>0x80000000000000</Keywords>
    <TimeCreated SystemTime="2014-06-25T06:56:04.000000000Z" />
    <EventRecordID>1294</EventRecordID>
    <Channel>Application</Channel>
    <Computer>WIN-2GTCJVJJS1T</Computer>
    <Security />
  </System>
  <EventData>
    <Data>python.exe</Data>
    <Data>0.0.0.0</Data>
    <Data>538b985c</Data>
    <Data>python27.dll</Data>
    <Data>2.7.7150.1013</Data>
    <Data>538b9859</Data>
    <Data>c0000005</Data>
    <Data>00031fe8</Data>
    <Data>1490</Data>
    <Data>01cf9042863370b8</Data>
    <Data>C:\Python27\python.exe</Data>
    <Data>C:\Windows\system32\python27.dll</Data>
    <Data>c5c1556d-fc35-11e3-b480-000c29e878b9</Data>
  </EventData>
</Event>