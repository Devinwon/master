import re
# 
ls=re.split(r'[1-9]\d{5}','BIT100081 CCNU100088')
print(ls)
# 分割一次，余下作为一整个字串
ls2=re.split(r'[1-9]\d{5}','BIT100081 CCNU100088',maxsplit=1)
print(ls2)