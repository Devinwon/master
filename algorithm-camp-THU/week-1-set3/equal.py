#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""




"""

# 数据组数
groupNum=int(input())
for _ in range(groupNum):
	varNum,condition=list(map(int,input().split()))
	equal=set()
	NOTequal=set()
	for x in range(condition):
		var,anothervar,r=list(map(int,input().split()))
		if r:
			equal.add(var)
			equal.add(anothervar)
		else:
			NOTequal.add(var)
			NOTequal.add(anothervar)
			# 1如果一个为全集，另一个非空，返回no
			# 2任意两个元素出现次数和大于1，返回no
	if len(equal)==0 or len(NOTequal)==0:
		# 特判
		print("Yes")
	else:
		# 全集
		full=set(x+1 for x in range(varNum))

		#补集 
		diff=full-equal
		if len(NOTequal-diff)>1:
			# 这里判断不正确
			print("No")
		else:
			print("Yes")



