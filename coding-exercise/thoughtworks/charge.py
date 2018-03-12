# charge
'''
周一——周五
09:00~12:00 30  
12:00~18:00 50  
18:00~20:00 80	
20:00~22:00 60	

周六周日
09:00~12:00 40
12:00~18:00 50
18:00~22:00 60
'''

#charge by time
from getweekday import get_week_day
def chargefee(day,timeblk):
	start=int(timeblk[:2])
	end=int(timeblk[6:8])
	fee=0
	day=get_week_day(day)
	# week day
	if day<5:
		if end<=12:
			fee=(end-start)*30
		elif end>12 and end<=18:
			if (end-start)<=6:
				fee=(end-start)*50
			else:
				fee=(end-12)*50+(12-start)*30
		elif end>18 and end <=20:
			if start<=12:
				fee=(12-start)*30+(18-12)*50+(end-18)*80
			elif start>12 and start<=18:
				fee=(18-start)*50+(end-18)*80
			else:
				fee=(end-start)*80
		elif end>20 and end<=22:
			if start<=12:
				fee=(12-start)*30+(18-12)*50+(20-18)*80+(end-20)*60
			elif start>12 and start<=18:
				fee=(18-start)*50+(20-18)*80+(end-20)*60
			elif start>18 and start<=20:
				fee=(20-start)*80+(end-20)*60
			elif start>20 and start<22:
				fee=(end-start)*60
	# weekend day
	else:
		if end<=12:
			fee=(end-start)*40
		elif end>12 and end<=18:
			if start<=12:
				fee=(end-12)*50+(12-start)*40
			elif start >12 and start<=18:
				fee=(end-start)*50
		elif end>18 and end <=22:
			if start>=18 and start<22:
				fee=(end-start)*60
			elif start>=12 and start <18:
				fee=(end-18)*60+(18-start)*50
			elif start<=12:
				fee=(12-start)*40+(18-12)*50+(end-18)*60
	return int(fee)





