"""
游戏
n:表示总人数,顺时针围圈
k:表示淘汰参数(报数为k倍数或者末尾为k)

解题思路:
人数使用列表:
条件使用函数或者简单语句均可

换一种思路
# done-----------------------------
n,k=list(map(int,input().strip().split()))
# 1表示都在圈内，0表示不在圈内，下标表示人员编号即可
peoplelst=[1 for n in range(n)]
count=0
flag=True
while flag:
	for inx in range(n):
		if peoplelst[inx]!=0:
			count+=1
			if count%k==0 or count%10==k :
				peoplelst[inx]=0
				# 去掉了人后，需要计算当前剩余人数 
				if sum(peoplelst)==1:
					flag=False
					break
for inx in range(n):
	if peoplelst[inx] :
		print(inx+1)
# -----------------------------
"""
# 通过使用队列实现
# -----------------------------
class Dequeue():
	def __init__(self):
		self.items=[]

	def size(self):
		return len(self.items)

	# 出队
	def deque(self):
		if len(self.items):
			t=self.items[0]
			self.items.remove(self.items[0])
		return t

	# 入队
	def enque(self,var):
		self.items.append(var)

n,k=list(map(int,input().strip().split()))
peoplelst=Dequeue()

for i in range(n):
	peoplelst.enque(i+1)

count=0
while peoplelst.size()>1:
	count+=1
	if count%k==0 or count%10==k :
		peoplelst.deque()
	else:
		peoplelst.enque(peoplelst.deque())

print(peoplelst.deque())





