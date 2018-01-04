'''
存在于文件中的大量用户参与抽奖进行程序修改

'''
# 从用户数据文件中抽取幸运用户

import random,time
import xlrd
'''
prize_item:奖项设置
user_data_file:参与抽奖用户数据文件名
lucky_dog:临时用于存储中奖用户的列表
'''
def lucky_draw(prize_item,user_data_file,lucky_dog):
	workbook=xlrd.open_workbook(user_data_file)
	# 默认为第一个工作页
	sheet=workbook.sheet_by_index(0)
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
	print("恭喜以上%d位获奖者"%len(lucky_dog))
	print("所有奖项抽取完毕，期待下次参与")
	

			



				