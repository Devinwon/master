# coding:utf-8
"""
1 ≤ n ≤ 1000，1 ≤ ai ≤ 1000。

约定中间数存在，输出那个数
否则，输出-1

排序，然后那中间的数字去比较就可以，不需要每个比较

考虑特殊情况：所有数都相等的情况，满足条件，大于小于==0
输出这个数字就可以

"""
n=int(input().strip())
numlst=list(map(int,input().strip().split()))
numlst.sort()
# 偶数个
def getmid(n,numlst):
	mid=-1
	if len(set(numlst))==1:
		mid=numlst[0]
	else:
		if n%2==0:
			if numlst.count(numlst[n//2])%2==0 :
				mid=numlst[n//2]
		else:
			if numlst.count(numlst[n//2])%2!=0 :
				mid=numlst[n//2]
	return mid

print(getmid(n,numlst))




