oddlst=[1,3,5]
# 引用
oddlst2=oddlst
print(oddlst)
print(oddlst2)

# 二者结果一样，指向了同一内容

oddlst[0]=7

print(oddlst)
print(oddlst2)

# 只对oddlst元素改变，oddlst2元素也受到了影响，更加说明指向同一内容

# 元组可以使用切片
t=(1,10,100,(11,12,))
t2=t[:]
print(t)
print(t2)

l=[1,2,[1,2]]
l2=l[:]
print(l)
print(l2)
# 对l中元素改变

l[2][0]=1000
print(l)
print(l2)

import copy
d={"add":"cn","cd":"10000","to":{"name":"Tom"}}
d2=copy.copy(d)
print(d)
print(d2)

d["add"]="usa"
print(d)
print(d2)








