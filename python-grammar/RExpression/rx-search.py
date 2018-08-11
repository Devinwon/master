import re
'''
# search() 
return the first match
rel.group()    type is string  
rel.group()  value is ccnu 
'''
s='6526526jdfjkshfjshccnuccuccnu'
reg="ccnu"
com=re.compile(reg)
rel=re.search(com,s)
print(type(rel))
print(rel)
print(type(rel.group()))
print(rel.group())
print(len(rel.group()))



