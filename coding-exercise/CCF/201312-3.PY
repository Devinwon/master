"""
最大的矩形

运行超时，40分

"""
n=int(input().strip())
height=list(map(int,input().strip().split()))
area=max(height)
for cnt in range(2,n+1):
	# 表示块的数量
	for i in range(n-cnt):
		temp=height[i:i+cnt]
		conn=min(temp)
		area=cnt*conn if cnt*conn>area else area

print(area)