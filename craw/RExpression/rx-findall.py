import re
'''
# findall() 
return all the matched  objects by list
rel    type is list  
'''
s='6526526jdfjkshfjshccnuccuccnu'
reg="ccnu"
com=re.compile(reg)
rel=re.findall(com,s)
print(type(rel))
print(rel)



