'''
检查申请是否有效,无效打印错误信息
有效更新预定信息表
'''

import db
from charge import chargefee
def checkApply(uid,bookdate,tmblock,placename):
	opOK=0
	'''资源占用标示'''
	placeFlag=dateFlag=0
	'''检查该场馆是否有预定'''
	ptemp=dtemp=''
	for plaindex in range(len(db.placeOrder)):
		if db.placeOrder[plaindex][0]==placename:
			'''该场馆有预定记录'''
			placeFlag=1
			ptemp=plaindex
			# print(placeFlag)
			break
	if placeFlag==1:
		'''该场地下该日期是否有申请记录'''
		for dteindex in  range(1,len(db.placeOrder[ptemp])):
			if bookdate==db.placeOrder[ptemp][dteindex][0]:
				'''该日期下有预定'''
				dateFlag=1
				dtemp=dteindex
				break
		if dateFlag==1:
			'''场地、日期下申请时段是否占用'''
			alltm=[]
			for i in range(1,len(db.placeOrder[ptemp][dtemp])):
				alltm+=db.placeOrder[ptemp][dtemp][i]
			if not set(alltm).intersection(set(list(range(int(tmblock[:2]),int(tmblock[6:8]))))):
				'''无交集，申请场地、日期内还有时段可以预定'''
				db.placeOrder[ptemp][dtemp].append(list(range(int(tmblock[:2]),int(tmblock[6:8]))))
				# 申请成功需要计费，
				db.total+=chargefee(bookdate,tmblock)
				opOK=1
			else:
				'''时段冲突预定失败'''
				opOK=4
		else:
			'''申请场地，日期内无预定记录，插入新日期，时段记录'''
			db.placeOrder[ptemp].append([bookdate,list(range(int(tmblock[:2]),int(tmblock[6:8])))])
			# 申请成功需要计费，
			db.total+=chargefee(bookdate,tmblock)

			# print(placeFlag)
			opOK=1
	else:
		'''申请场地无任何预定,申请成功，插入信息'''
		db.placeOrder.append([placename,[bookdate,list(range(int(tmblock[:2]),int(tmblock[6:8])))]])
		# 申请成功需要计费，更新db.userPlace,将地点加入
		db.total+=chargefee(bookdate,tmblock)

		ufound=False
		utemp=''
		for uindex in range(len(db.userPlace)):
			if uid ==db.userPlace[uindex][0]:
				ufound=True
				utemp=uindex
				break
		if not ufound:
			db.userPlace.append([uid,[placename]])
		else:
			# 存在用户，检查是否申请有场地
			if placename not in db.userPlace[utemp][1]:
				db.userPlace[utemp][1].append(placename)
		opOK=1
	return opOK
