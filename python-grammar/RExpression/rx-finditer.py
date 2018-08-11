import re
'''
# finditer() 
return all the matched  objects by iterator
rel    type is iterator  
'''
s='azcbobobebobobgghakl'
reg="b(ob)+"
com=re.compile(reg)
rel=re.finditer(com,s)
# print(type(rel))
# print(rel)
cnt=0
for _ in rel:
	if len(_.group())==3:
		cnt+=1
	else:
		cnt+=(len(_.group())-1)//2
print(cnt)

