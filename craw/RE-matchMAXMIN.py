import re
# 贪婪匹配(默认) 非贪婪匹配
# 增加？获得最小匹配
rel=re.match(r'PY.*N','PYANBNCNDN')

rel2=re.match(r'PY.*?N','PYANBNCNDN')
print(rel.group(0))
print(rel2.group(0))
