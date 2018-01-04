'''
初始化如下列表
alist = [20170123, 61, 20170233, 97， 20170123， 72， 
					20170233， 65， 20170110， 97]

该列表中下标为偶数的元素表示某个学生的学号，
其后紧跟着的下标为奇数的元素表示该学生某门课程的成绩。
编程对该列表进行重新排序。（不限制使用函数或列表方法）
要求：
1、保持一个学号紧跟着一个成绩的数据格式不变
2、以学号按升序排列，当学号相同时，以成绩按降序排列
'''
alist = [ 20170123, 61, 
					20170233, 97, 
					20170123, 72, 
					20170233, 65, 
					20170110, 97
				]

while True:
	if type(alist[-1])==int:
		score=alist.pop()
		idno=alist.pop()
		alist.insert(0,[idno,score])
		# print(alist)
	else:
		break

alist.sort()
def cmp(lst):
	for i in range(len(lst)-1):
		for j in range(i+1,len(lst)):
			if lst[i][0]==lst[j][0] and lst[i][1]<lst[j][1]:
				# print(lst[i][0])
				lst[i],lst[j]=lst[j],lst[i]
	return lst

alist=cmp(alist)[:]
while True:
	if type(alist[-1])==list:
		score_idno=alist.pop()
		score=score_idno[1]
		idno=score_idno[0]
		alist.insert(0,score)
		alist.insert(0,idno)
	else:
		break
print(alist)