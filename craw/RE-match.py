import re
# 从头（起始位置）匹配，只返回一个结果
rel=re.match(r'[1-9]\d{5}','100081 BIT 100088')
if rel:
	print(rel.group(0))
