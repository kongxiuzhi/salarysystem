#coding:utf-8
import pymysql.cursors
from openpyxl import load_workbook
from django.utils import timezone
from django.http import HttpResponse

now = timezone.now()

datas = [(3,"zhi"),(4,"zhubajie"),(5,"shaseng")]
connection = pymysql.connect(
			host='localhost',
			#user='user1',
			user='salarydbuser',
			password='1234567890',
			#db='testdb',
			db='salarydb',
			charset='utf8mb4',
			cursorclass=pymysql.cursors.DictCursor
	)


salartfields = """

(salarytime,gwgz,zjjt,zwjt,blgz,nggz,dqlcjt,wpjt,tgjt,gwgt,
yjgz1,yjgz2,jbf,cybjt,cdztkk,kgkk,bjkk,sjkk,zjljlj,xmjlj,
jhhj,tabc,bjf,sqbf,sqkk,yfgz,yanglbxgr,sybxge,yilbxgr,
zfgjjgr,qynjgrjfsqkk,qynjgrjfsqbk,gzxzgrsds,dsznf,kckk,
jtzf,qynjgrjfshkk,qynjgrjfshbk,shbf,shkk,sfgz,created,updated,staffnum_id)

"""




def getfiledata(filename):
	wb = load_workbook(filename)
	ws = wb.active
	dataDict = {}
	ctn = 0
	for row in ws.rows:
		dataDict[ctn]=[]
		for cel in row:
			dataDict[ctn].append(cel.value)
		ctn+=1
	del(dataDict[0])
	return dataDict


def insert(filename,action):
	try:
		with connection.cursor() as cursor:
			jumpctn = 0
			#print(filename)
			datas = getfiledata(filename)
			if action == "1":
				sql1 = "select * from show_user where staffnum=%s"
				sql = "insert into show_user (staffnum,username,idcard,banknum,password,active,created,updated) values (%s,%s,%s,%s,%s,%s,%s,%s)"
				for i in datas:
					cursor.execute(sql1,datas[i][0])
					if cursor.fetchone():
						print("jump")
						print(jumpctn)
						continue
					cursor.execute(sql,tuple(datas[i]+[datas[i][2][-7:-1],0,now,now]))	
					connection.commit()	
					


			if action == "2":
				print('testerror')
				sql1 = "select * from show_salary where staffnum_id=%s and salarytime=%s"
				sql = "insert into show_salary" + salartfields + "values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
				for i in datas:
					cursor.execute(sql1,(datas[i][0],datas[i][1]))
					print((datas[i][0],datas[i][1]))
					if cursor.fetchone():
						print("jump")
						continue
				
					print(tuple(datas[i][1:]+[now,now,datas[i][0]]))
					print(sql)
					cursor.execute(sql,tuple(datas[i][1:]+[now,now,datas[i][0]]))	
					connection.commit()	

			#elif action == "2":
				#sql = "insert into show_salary (username,staffnum,idcard,password,banknum,active,created,updated) values (%s,%s,%s,%s,%s,%s,%s,%s)"
			#sql = "insert into tb (id,name) values (%s,%s)"

			#sql = "select * from show_user"
		
			#cursor.execute(sql,i)
			#connection.commit()
			#result = cursor.fetchone()
			cursor.close()
			connection.close()
	
	except:
		print('error')