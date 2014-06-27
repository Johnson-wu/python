#coding:utf-8

from ctypes import *
import threading
import time,datetime
import psycopg2 as postgres
import psycopg2.pool as pool
import logging

PATH = ''
CONNECT_PARAM = 'dbname=xincloud1.0.1 user=postgres password=root host=1.1.1.115'

def generateLogger():
	FORMAT = '%(asctime)s - %(levelname)s - %(module)s : %(message)s'
	logging.basicConfig(filename='IDReader.log',format=FORMAT)
	loger = logging.getLogger('root')
	return loger


def generateConnPool():
	return pool.SimpleConnectionPool(5,5,CONNECT_PARAM)


def insertIDInfo(conn,dic,loger):
	try:
		birthday = dic['birthday']
		year = int(birthday[:4])
		month = int(birthday[4:6])
		day = int(birthday[6:])
		# date = datetime.date(year,month,day)
		# dic['birthday'] = date
		conn = postgres.connect(CONNECT_PARAM)
		cur = conn.cursor()
		cur.execute('INSERT INTO gnuhealth_registration (name,sex,birthday,speciality,registration_type,pinyin) VALUES(%s,%s,%s,%s,%s,%s)',\
						(dic['name'],dic['gender'],postgres.Date(year,month,day),63,1,'a'))
		# cur.execute('INSERT INTO gnuhealth_registration (name,sex,birthday,speciality,registration_type,pinyin) VALUES(%s,%s,%s,%s,%s,%s)',(dic['name'],dic['gender'],dic['birthday'],63,1,'a'))
		print 'insert successfully...'
		conn.commit()
	except Exception, e:
		conn.rollback()
		loger.exception(e)
	

def getIDInfos(dll,connPool,loger):
	while True:	
		try:
			res = dll.InitComm(c_int(1001))

			if res == 1:
				# print 'device is ready...'
				auth_res = dll.Authenticate()

				if auth_res == 1:
					# print 'ID card is ready...'
					name = 'a'*32
					gender = 'b'*4
					folk = 'c'*11
					birthday = 'd'*10
					code = 'e'*20
					addr = 'f'*72
					agency = 'g'*32
					expireStart = 'h'*10
					expireEnd = 'i'*10

					p_name = c_char_p(name)
					p_gender = c_char_p(gender)
					p_folk = c_char_p(folk)
					p_birthday = c_char_p(birthday)
					p_code = c_char_p(code)
					p_addr = c_char_p(addr)
					p_agency = c_char_p(agency)
					p_expireStart = c_char_p(expireStart)
					p_expireEnd = c_char_p(expireEnd)

					result = dll.ReadBaseInfos(p_name,p_gender,p_folk,p_birthday,p_code,p_addr,p_agency,p_expireStart,p_expireEnd)

					if result == 1:
						dic = {
							'name': p_name.value.decode('gbk').encode('utf-8').strip(),
							'gender': p_gender.value.decode('gbk').encode('utf-8').strip(),
							'folk': p_folk.value.decode('gbk').encode('utf-8').strip(),
							'birthday': p_birthday.value,
							'address': p_addr.value.decode('gbk').encode('utf-8').strip(),
							'agency': p_agency.value.decode('gbk').encode('utf-8').strip(),
							'expireStart': p_expireStart.value,
							'expireEnd': p_expireEnd.value
						}

						if p_gender.value.decode('gbk').encode('utf-8').strip() == '男':
							dic['gender'] = 'male'
						else:
							dic['gender'] = 'female'

						conn = connPool.getconn()
						insertIDInfo(conn,dic,loger)			
		except Exception, e:
			loger.exception(e)
		time.sleep(1)
		


if __name__ == '__main__':
	try:
		loger = generateLogger()
		connPool = generateConnPool()
		dll = windll.LoadLibrary('sdtapi.dll')
		print 'load dll successfully...'
		threading.Thread(target=getIDInfos, args=(dll,connPool,loger)).start()
	except Exception, e:
		loger.exception(e)
		connPool.closeall()

	