"""
题目很长，




"""

m,l,r=list(map(int,input().strip().split()))
klst=list(map(int,input().strip().split()))
# m=len(klst)
Q=998244353
# 初始化a[]
a=[ 0 for _ in range(r+1)]
a[0]=1
for i in range(1,r+1):
	temp=i
	for j in range(m):
		a[i]+=klst[j]*a[temp-1]
		temp-=1
	a[i]=a[i]%Q

for inx in range(l,r+1):
	print(a[inx])