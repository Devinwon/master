'''
db.userPlace=[
						[userid,[placeA,placeB]],
						[userid2,[placeA,placeB]],
						]
db.placeOrder=[
						['A',['2009-10-1',[9,10,11]],['2010-11-1',[20,21,22]]] 

						]
'''
import db
from charge import chargefee
from getweekday import get_week_day
def checkCancle(uid,bookdate,tmblock,placename):
	cancelOK=0
	utemp=''
	uflag=0
	for uindex in range(len(db.userPlace)):
		if db.userPlace[uindex][0]==uid:
			# 用户有申请记录
			utemp=uindex
			uflag=1
			break

	if uflag:
		if placename not in db.userPlace[utemp][1]:
			# 有用户，无场地记录，却要取消对应场地预定，报错:取消了不存在的申请
			cancelOK=-2
		else:
			# 用户场地匹配，检查日期，时段是否匹配？
			# 有匹配预定，可以取消
			ptemp=''
			dtemp=''
			for plaindex in range(len(db.placeOrder)):
				if db.placeOrder[plaindex][0]==placename:
					#找到场馆			 
					placeFlag=1
					ptemp=plaindex
					break
			dateFlag=0
			for dteindex in  range(1,len(db.placeOrder[ptemp])):
				if bookdate==db.placeOrder[ptemp][dteindex][0]:
					'''找到日期'''
					dateFlag=1
					dtemp=dteindex
					break
			if dateFlag==0:
				# 没找到要取消的日期记录
				cancelOK=-3
			else:
				# 匹配时段
				if list(range(int(tmblock[:2]), int(tmblock[6:8]))) in (db.placeOrder[ptemp][dtemp][1:]):
					# 取消成功,收取违约金
					if get_week_day(bookdate)>4:
						db.total-=chargefee(bookdate,tmblock)*0.75
					else:
						db.total-=chargefee(bookdate,tmblock)*0.5
					#将预定删除,还需要考虑前置资源-日期,场地,用户,
					db.placeOrder[ptemp][dtemp].remove(list(range(int(tmblock[:2]), int(tmblock[6:8]))))
					if len(db.placeOrder[ptemp][dtemp])==1:
						# 删除日期
						db.placeOrder[ptemp].remove(db.placeOrder[ptemp][dtemp])
					if len(db.placeOrder[ptemp])==1:
						# 删除场地
						db.placeOrder.remove(db.placeOrder[ptemp])
						# 删除场地
						db.userPlace[utemp][1].remove(placename)
						# []空列表
						if len(db.userPlace[utemp][1])==0:
							db.userPlace.remove(db.userPlace[utemp])
					cancelOK=1
				else:
					# 没有要取消的时段
					cancelOK=-4

	else:
		# 用户无任何申请，却要取消
		cancelOK=-1
	return cancelOK
			