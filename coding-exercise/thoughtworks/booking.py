
from datecheck import dateCheck
from timeblock import check_timeblock
from checkplace import checkPlace
from checkapply import checkApply
from checkCancel import checkCancle
import db

uid=bookdate=tmblock=placename=cancelFlag=''
def main():
	cmdlist=input().split()
		# apply operation 
	if len(cmdlist)==4:
		uid,bookdate,tmblock,placename=cmdlist
		if uid!='' and dateCheck(bookdate) and check_timeblock(tmblock) and checkPlace(placename):
			# 调用申请函数
			rel=checkApply(uid,bookdate,tmblock,placename)
			if rel==-1:
				print('Error: the booking is invalid!')
			elif rel==1:
				print("Success: the booking is accepted!")
			elif rel==4:
				print("Error: the booking conflicts with existing bookings!")
		else:
			print('Error: the booking is invalid!')
	elif len(cmdlist)==5:
		try:
			uid,bookdate,tmblock,placename,cancelFlag=cmdlist
			if uid!='' and dateCheck(bookdate) and check_timeblock(tmblock) and checkPlace(placename) and cancelFlag=='C':
				# 调用取消函数
				rel=checkCancle(uid,bookdate,tmblock,placename)
				if rel<0:
					print("Error: the booking being cancelled does not exist!")
				elif rel:
					print("Success: the booking is accepted!")
			else:
				print('Error: the booking is invalid!')
		except:
			print('Error: the booking is invalid!')
			pass
	elif len(cmdlist)==0:
		print('收入汇总')
		print('---')
		print("场地:A")
		print("场地:B")
		print("场地:C")
		print("场地:D")
		print('---')
		print('总计:%s'%db.total)
		# 调用汇总函数
	else:
		print('Error: the booking is invalid!')

while True:
	main()
	# print(db.userPlace)
	# print(db.placeOrder)

	
