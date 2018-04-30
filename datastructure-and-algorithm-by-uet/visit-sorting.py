import random
from operator import itemgetter, attrgetter
la=[int(random.random()*100) for _ in range(20)]
# print(la)
rel={}
for _  in range(1000):
	t=random.choice(la)
	# 原先有就+1
	# 没有就初始化为1
	rel[t]=rel[t]+1 if rel.get(t,0) else 1
	# rel[t]=rel[t]+1 if t in rel else 1
# print(rel)
sortLst=sorted(rel.items(), key=itemgetter(1), reverse=True)
# print(sortLst)
print("1-99之间的数字随机访问频次/1000")
for v in sortLst:
	print("{:0>2}".format(str(sortLst.index(v)+1)), "{:0>2}".format(str(v[0])),v[1]//2*'-',v[1])
	# 右对齐,0填充