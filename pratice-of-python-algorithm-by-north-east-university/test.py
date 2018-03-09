'''
varA=input()
varB=int(input())
# print(type(varA)==str)
# type(varA)==str 这样比较
if type(varA)==type('a') or type(varB)==type('a'):
    print("string involved")
elif varA>varB:
    print("bigger")
elif varA==varB:
		print('equal')
else:
		print('smaller')
		'''

'''
def getsum(*var):
	if var is None:
		return 0
	else:
		s=0
		for v in var:
			s+=v
		return s

print(getsum(1,2,3))
print(getsum())


def profile():
    name = "Danny"
    age = 30
    return name, age

print(type(profile()))
print(profile())
print(profile()[0])
print(profile()[1])
'''
def nameEdit(name="张三"):
    def ori():
        return "默认名为张三"

    def after():
        return "你修改了默认名"

    if name == "张三":
        return ori
    else:
        return after
# 改变参数指向不同的函数
nm = nameEdit()
print(nm)
print(nm())

nm = nameEdit(name="Jame")
print(nm)
print(nm())