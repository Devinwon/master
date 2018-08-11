import re
"""
finditer可以迭代匹配,其他的不能迭代匹配
"""
s='azcbobobegghakl'
reg="ba(ob)+"
com=re.compile(reg)
rel=re.finditer(com,s)
cnt=0
for _ in rel:
	if len(_.group())==3:
		cnt+=1
	else:
		cnt+=(len(_.group())-1)//2
print "Number of times bob occurs is: {}".format(cnt)
