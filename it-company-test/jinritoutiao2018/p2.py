libNum,itemNum=list(map(int,input().split()))
lib=[]
item=[]
for _ in range(libNum):
	t=input()
	lib.append(t)
print('')
for _ in range(itemNum+1):
	t=input()
	if t:
		item.append(t)
# 结果之间有空行
def search(lib,item):
	found=[-1 for _ in range(len(item))]
	for index in range(len(item)):
		for lb in lib:
			if item[index].startswith(lb):
				found[index]=-found[index]
				continue
	return found

for v in search(lib,item):
	print(v)
print()




