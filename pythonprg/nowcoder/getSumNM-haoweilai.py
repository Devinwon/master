'''
输入两个整数n和m，从自然数1——n中随意取几个数,
使其和等于 m ,
所有的可能组合列出来,如
5 5

1 4
2 3
5

动态向后遍历（有序）过程，逻辑分支需要细分
6 8没有通过
'''

num=list(input().split())
N=int(num[0])
numlst=list(range(1,N+1))
M=int(num[1])
# print('N,M',N,M)
def prtrel(lst):
	if len(lst)==1:
		print(lst[0])
	else:
		print(lst[0],end='')
		for val in lst[1:]:
			print(' ',val,end='',sep='')
		print()

def getsum(lst):
	sum=0
	for val in lst:
		sum+=val
	return sum
# print('numlst',numlst)

thesum=M
rel=[]
# 始终把握numlst否全部遍历，
while(numlst and thesum>=numlst[0] and thesum<=getsum(numlst)):
	# 每次重置M,rel
	M=thesum
	rel=[]
	for length in range(len(numlst)):
		if M-numlst[length]>0:
			#更新M,存储
			M=M-numlst[length]
			rel.append(numlst[length])
			if M in numlst[length+1:]:
				rel.append(M)
				prtrel(rel)
				# print(rel)
				numlst=numlst[1:]
				break
				# 一次满足条件的遍历结束

		elif M-numlst[length]==0:
			# 以上针对边界情况
			rel.append(M)
			prtrel(rel)
			# print(rel)
			numlst=numlst[1:]

		else:
			# 不满足并不能确定后续也不满足
			numlst=numlst[1:]
			break

			