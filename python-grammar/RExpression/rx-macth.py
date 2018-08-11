import re
'''
# macth 
match from just the start
rel.group()    type is string  
rel.group()  value is ccnu 
'''
s='ccnu6526526jdfjkshfjshccnucunu'
reg="ccnu"
com=re.compile(reg)
rel=re.match(com,s)
print(type(rel))
print(rel)
print(type(rel.group()))
print(rel.group())



