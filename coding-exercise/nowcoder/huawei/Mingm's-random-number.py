'''
title:
明明的随机数

#description:#
明明想在学校中请一些同学一起做一项问卷调查，
为了实验的客观性，他先用计算机生成了N个1到1000之间的随机整数（N≤1000），
对于其中重复的数字，只保留一个，把其余相同的数去掉，
不同的数对应着不同的学生的学号。然后再把这些数从小到大排序，
按照排好的顺序去找同学做调查。请你协助明明完成“去重”与“排序”的工作。

###Input description###
输入多行，先输入随机整数的个数，再输入相应个数的整数 
注意存在多组数据

###Output description###
返回多行，处理后的结果

#example#

###Input###
11
10
20
40
32
67
40
20
89
300
400
15

###Output###
10
15
20
32
40
67
89
300
400
'''
'''
total=int(input())
rel=[]
while total:
	random_number=int(input())
	if random_number not in rel:
		rel.append(random_number)
	total-=1

rel.sort()
print()
for v in rel:
	print(v)

'''

'''

while True:
	try:
		total=int(input())
		rel=[]
		while total:
			random_number=int(input())
			rel.append(random_number)
			total-=1
		rel=list(set(rel))
		rel.sort()
		for v in rel:
			print(v)
	except:
		break
'''
while True:
	try:
		total=int(input())
		rel=set()
		while total:
			rel.add(int(input()))
			total-=1
		for v in sorted(list(rel)):
			print(v)
	except:
		break

