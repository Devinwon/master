import re
'''
# finditer() 
return all the matched  objects by iterator
rel    type is iterator  
'''
s='6526526jdfjkshfjshccnuccuccnu'
reg="ccnu"
com=re.compile(reg)
rel=re.finditer(com,s)
print(type(rel))
print(rel)
for _ in rel:
	print(_.group())


