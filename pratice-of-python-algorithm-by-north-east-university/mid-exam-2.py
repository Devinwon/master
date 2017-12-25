'''
从键盘连续输入5名同学的学号和3门不同科目的考试成绩，
找到总分最高的同学，
输出他（她）三门课程的成绩、总分及平均分。

1-对总的人数、科目进行了灵活处理，没有写死
2-对重复性学号做了检查
3-对并列高分进行了统一输出
'''
def id_unique(sid,id_db):
	flag=True
	if id_db:
		for v in id_db:
			if sid==v[0]:
				flag=False
				break
	return flag

total=2
subject_item=["科目1","科目2","科目3"]
subjects=len(subject_item)
marksdb=[]
print('--学生成绩录入操作中--\n')
num=0
while num<total:
	stu_id=input('\n输入第%d/%d名学生的学号:'%(num+1,total))
	# 学号重复性检查,
	if id_unique(stu_id,marksdb):
		sub=0
		marksdb.append([stu_id])
		num=num+1
		while sub<subjects:
			sub_mark=eval(input('学号%s学生%s成绩输入:'%(stu_id,subject_item[sub])))
			sub=sub+1
			marksdb[-1].extend([sub_mark])
		# print("当前学生成绩表",marksdb)
	else:
		print('学号%s已经存在，重新输入其他学号'%stu_id)

sumofmarks=0
index=0
for v in marksdb:
	# 寻找总分最高的学生
	if sumofmarks<sum(v[1:]):
		sumofmarks=sum(v[1:])
		index=marksdb.index(v)

# 输出最高分学生信息
print("\n===总分最高学生信息如下===\n")
print("学号\t%s\t总分\t平均分\t"%("\t".join(subject_item)))
# 多个并列高分的判断输出
for item in marksdb:
	if sum(item[1:])==sumofmarks:
		print(item[0],end='\t')
		for s in range(subjects):
			print(item[s+1],end='\t\t')
		print(sumofmarks,end='\t\t')
		print('%.2f'%(sumofmarks/subjects))
