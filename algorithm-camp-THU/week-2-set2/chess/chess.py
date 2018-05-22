#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
"""
对棋盘扫描,X,Y方向,最小的行列>1放置元素

放置后,同一行的其他位置归0,题目要求

不知道是否可行

5
1 0 0 0 0
0 0 0 0 0
0 0 0 1 0
1 1 0 1 0
0 0 0 1 0

车 0 0 0 0
0 0 0 0 0
0 0 0 1 0
1 车 0 1 0
0 0 0 车 0

"""
def sumOf(lst,x,y):
	sumX=sum(lst[x])
	sumY=0
	for i in range(len(lst)):
		sumY+=lst[i][y]
	return (sumX,sumY)


n=int(input.strip())
lst=[]
for _ in range(n):
	temp=list(map(int,input.strip().split()))
	lst.append(temp)

total=0
for  i in range(n):
	for j in range(n):
		if lst[i][j]:
			x,y=sumOf(lst,i,j)
			if x<y:
				total+=1
				# (i,j)行列其他元素置为0




