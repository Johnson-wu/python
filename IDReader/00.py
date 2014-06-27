#coding:utf-8
import datetime
# print b'\xce\xe2\xbe\xa4'.decode('gb2312')

st = '\xce\xe2\xbe\xa4'

print st.decode('gbk').encode('utf-8')
# print st.decode('gbk').encode('gbk')


# 将一个字典实例序列化为一个json字串
# Serialize obj to a JSON formatted str using this conversion table.
# If ensure_ascii is False, the result may contain non-ASCII characters and the return value may be a unicode instance.
# json_str = json.dumps(dic,ensure_ascii=False)
# print json_str

# # 对json字串反序列化为为一个python object
# # Deserialize s (a str or unicode instance containing a JSON document) to a Python object using this conversion table
# json_obj = json.loads(json_str,encoding='gbk')

# # 取出字典中的某个key对应的value
# print json_obj['name']

date = datetime.date(1990,12,2)
print type(date)

yr = int('1990')
mo = int('12')
day = int('2')
date2 = datetime.date(yr,mo,day)
print type(date2),date2