import math
def  leapyear(year):
    if(year%400==0 or (year%4==0 and year%100!=0)):
        return 1
    else:
        return 0
thedate=input("input the date:")
# 将年月日进行分
dtlist=thedate.split('-')
theyear=int(dtlist[0])
themonth=int(dtlist[1])
theday=int(dtlist[2])
orderdayIndex=0
dayinMonth=[31,28,31,30,31,30,31,31,30,31,30,31]

for i in range(themonth-1):
    orderdayIndex=orderdayIndex+dayinMonth[i]
if(leapyear(theyear) and themonth>2):
    orderdayIndex=orderdayIndex+1
print("The day:",orderdayIndex+theday)
