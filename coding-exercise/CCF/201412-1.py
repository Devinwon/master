# coding:utf-8

"""
门禁系统

问题描述
　　涛涛最近要负责图书馆的管理工作，需要记录下每天读者的到访情况。每位读者有一个编号，
每条记录用读者的编号来表示。给出读者的来访记录，请问每一条记录中的读者是第几次出现。

输入格式
　　输入的第一行包含一个整数n，表示涛涛的记录条数。
　　第二行包含n个整数，依次表示涛涛的记录中每位读者的编号。
输出格式
　　输出一行，包含n个整数，由空格分隔，依次表示每条记录中的读者编号是第几次出现。
样例输入
5
1 2 1 1 3
样例输出
1 1 2 3 1
评测用例规模与约定
　　1≤n≤1,000，读者的编号为不超过n的正整数。

如果不用counter函数需要使用字典完成，记录每次的


n=int(input().strip())
nlst=list(map(int,input().strip().split()))
rel=[]
for inx in range(n):
	t=str(nlst[:inx+1].count(nlst[inx]))
	rel.append(t)
print(' '.join(rel))

"""
n=int(input().strip())
nlst=list(map(int,input().strip().split()))
rel={}

if n>1:
	for v in nlst[:-1]:
		if v in rel:
			# 已经存在
			rel[v]+=1
			print(rel[v],'',end='')
		else:
			# 第一次出现
			rel[v]=1
			print(rel[v],'',end='')

	# 最后一个数，格式控制
	if nlst[-1] in rel:
		print(rel[nlst[-1]]+1)
	else:
		print(1)
else:
	print(1)
