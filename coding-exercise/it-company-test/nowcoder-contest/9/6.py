'''
珂朵莉给你一个长为n的序列，有m次查询
每次查询给两个数l,r
设s为区间[l,r]内所有数的乘积
求s的约数个数mod 1000000007
输入描述:
第一行两个正整数n,m
第二行一个长为n的序列
之后m行每行两个数l和r
输出描述:
对于每个询问，输出一个整数表示答案
本地通过，nowcoder没有通过

5 5
64 2 18 9 100
1 5
2 4
2 3
1 4
3 4
输出

165
15
9
45
10
'''
import math
def getfactors(sublst):
	m=1
	for v in sublst:
		m*=int(v)
	cnt=2
	for f in range(2,int(math.sqrt(m))):
		if m%f==0:
			cnt+=2
	if m%(math.sqrt(m))==0:
		cnt+=1
	return cnt


n,m=input().split()
n,m=int(n),int(m)
n_lst=list(input().split())
query=0
rel=[]
while query<m:
	l,r=input().split()
	l,r=int(l)-1,int(r)
	rel.append(getfactors(n_lst[l:r]))
	query+=1
	# 查询输出结果
for ve in rel:
	print(ve)


