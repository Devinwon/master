"""
merge list
"""
import random
la=[int(random.random()*100) for _ in range(5)]
lb=[int(random.random()*100) for _ in range(5)]



def mergeLst(la,lb):
	# 注意extend将la改变了
	la.extend(lb)
	return la

def mergeLstMod(la,lb):
	# 保留原来的数组,不用函数实现
	lc=la[:]
	for v in lb:
		lc.append(v)
	return lc

def mergeLstSorted(la,lb):
	# 保留原来的数组,有序合并
	la.sort()
	lb.sort()
	print(la)
	print(lb)
	# 较少的数据插入
	rel=la[:] if len(la)>=len(lb) else lb[:]
	toinser=la[:] if len(la)<len(lb) else lb[:]
	for v in toinser:
		for i in range(len(rel)-1):
			if v<rel[0]:
				rel.insert(0,v)
				break
			elif v>rel[-1]:
				rel.append(v)
				break
			else:
				if rel[i]<=v<=rel[i+1]:
					rel.insert(i+1,v)
					break
	return rel

print(mergeLstSorted(la,lb))