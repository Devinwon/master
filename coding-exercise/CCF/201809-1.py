"""
n>=2,商店数量

第一天每个菜商的价格

firstDayprice=[]

求每个菜商第二天的菜价
"""
n=int(input().strip())
firstDayprice=list(map(int,input().strip().split()))
ret=[0 for _ in range(n)]
for i in range(n):
	if i==0:
		ret[i]=(firstDayprice[i]+firstDayprice[i+1])//2
	elif i==n-1:
		ret[i]=(firstDayprice[i]+firstDayprice[i-1])//2
	else:
		ret[i]=(firstDayprice[i+1]+firstDayprice[i]+firstDayprice[i-1])//3
for inx in range(n-1):
	print(ret[inx],'',end='')
print(ret[-1])


