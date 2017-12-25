import re
# 列表形式返回所有匹配的字串
'''
regex=re.compile(r'[1-9]\d{5}')
rel=regex.findall('BIT100081 CCNU100088')
'''

ls=re.findall(r'[1-9]\d{5}','BIT100081 CCNU100088')
print(ls)
