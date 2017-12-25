import re
# 迭代对每一个结果进行处理
for m in re.finditer(r'[1-9]\d{5}','BIT100081 CCNU100088'):
	if m:
		print(m.group(0))
