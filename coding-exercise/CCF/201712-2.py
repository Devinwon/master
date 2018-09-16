"""
游戏
n:表示总人数,顺时针围圈
k:表示淘汰参数(报数为k倍数或者末尾为k)

解题思路:
人数使用列表:
条件使用函数或者简单语句均可

换一种思路
"""
n,k=list(map(int,input().strip().split()))
peoplelst=[n for n in range(1,n+1)]
start=0

while n>1:
	peoplelstbak=peoplelst[::] 
	for inx in range(1+start,n+1+start):
		if inx%10==k or inx%k==0:
			# peoplelst已经改变了,不能对应原来的索引
			peoplelst.remove(peoplelstbak[inx-start-1])
			n-=1
	print('每轮循环完后,数据',peoplelst)
	print('每轮循环完后,数据bak',peoplelstbak)
	start+=len(peoplelstbak)
	# print('start,n',start,n)
print(peoplelst[0])



