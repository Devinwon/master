# 看他后面是否都是1，是的话就是Alice

cnt=int(input())
status=list(input().split())
index=status.index('1')
rel=1
for i in range(index+1,cnt):
	if status[i]!='1':
		rel=0
		break
if rel:
	print("Alice")
else:
	print("Bob")