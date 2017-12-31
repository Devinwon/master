# 点的个数
N=int(input())
# 接下来输入点的坐标
pointset=[]
for i in range(N):
	pset=list(input().split())
	pointset.append((int(pset[0]),int(pset[1])))

# 排序
pointset.sort()
# 记录满足条件的
print(pointset)
relset=[]

for le in range(len(pointset)):
	flag=True
	for be in pointset[le+1:]:
		if be[1] > pointset[le][1]:
			flag=False
			break
	if flag:
		relset.append(pointset[le])

for v in relset:
	print(v[0],v[1])
