'''
存在于文件中的大量用户参与抽奖进行程序修改

'''

import random,time
import xlrd
from  writetotxt import writeTotxt 

prize_item=[["三等奖",3],["二等奖",2],["一等奖",1]]

workbook=xlrd.open_workbook("user.xls")
sheet=workbook.sheet_by_index(0)
lucky_dog=[]

for pv in prize_item:
	count=0
	while count<pv[1]:
		for row in range(1,sheet.nrows):
			t=random.randint(1,100000)
			nmstr=str(sheet.row(row)[0])
			if t%2018==0:
				winner=eval(nmstr[5:])
				if winner not in lucky_dog:
					lucky_dog.append(winner)
					print("恭喜%s中奖者:%s"%(pv[0],winner))
					count+=1
					time.sleep(2)
	print()
# 将中奖者信息写入文件备份
writeTotxt(lucky_dog)
print("恭喜以上%d位获奖者"%len(lucky_dog))
print("所有奖项抽取完毕，期待下次参与")

			



				