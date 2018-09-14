"""
最小差值

问题描述

　　给定n个数，请找出其中相差（差的绝对值）最小的两个数，输出它们的差值的绝对值。

输入格式

　　输入第一行包含一个整数n。
 　　第二行包含n个正整数，相邻整数之间使用一个空格分隔。

输出格式

　　输出一个整数，表示答案。

解题思路:
正整数,不考虑负数

排序后相邻计算,算法0(n)

能优化吗?
不能
"""
cnt=int(input().strip())
numlst=list(map(int,input().strip().split()))
numlst.sort()

# print(numlst)
# 初始化不正确,影响后面的值比较
mindiff=abs(numlst[0]-numlst[1])
cnt-=1
while cnt>=2:
	if mindiff==0:
		break
	t=abs(numlst[0]-numlst[1])
	mindiff=t if t<mindiff else mindiff
	cnt-=1
	numlst=numlst[1:]

print(mindiff)
