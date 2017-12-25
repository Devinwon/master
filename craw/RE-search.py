import re
rel=re.search(r'[1-9]\d{5}','BIT 100081')
if rel:
	print(rel.group(0))

'''
rel.pos
rel.endpos
rel.group(0)
rel.start()
rel.end()
rel.span()

'''
