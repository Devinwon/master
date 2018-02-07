'''
字典是无序的
键-值对
'''
info={"add":"SZ","class":"lvl1"}
for k,v in info.items():
	print(k,v)

print(info.get("gender","Male"))
print(info)
info.setdefault("gender","female")
print(info)