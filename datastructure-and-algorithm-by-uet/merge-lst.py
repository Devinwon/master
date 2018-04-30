"""
merge list
"""
import random
la=[int(random.random()*100) for _ in range(5)]
lb=[int(random.random()*100) for _ in range(5)]
print(la)
print(lb)


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
print(mergeLst(la,lb))