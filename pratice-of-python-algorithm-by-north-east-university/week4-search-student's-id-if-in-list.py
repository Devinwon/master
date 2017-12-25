'''
针对成绩列表[[201,77],[202,82],[203,93],[204,87],[205,88],[206,91]]，
编写程序，输入学号，输出其成绩，如学号不存在于此列表中，给出提示信息。
'''
print("---学生成绩查询应用---\n")
marks_db=[[201,77],[202,82],[203,93],[204,87],[205,88],[206,91]]
while True:
	#print("请输入你要查询的学号：按Q退出应用\n")
	search=input("输入学号查询：按Q退出应用\n")
	if search=='Q'or search=='q':
		print("退出应用")
		break 
	else:
		found=False
		for mks in marks_db:
			if str(mks[0])==search:
				print("学号%s的学生成绩为:%s\n"%(str(mks[0]),str(mks[1])))
				found=True
				break
		if not found:
			print("没有找到对应的学号，请重新确认后输入\n")