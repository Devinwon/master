'''
列表的一些方法
'''
lst=[1,2,3,"male","female"]

'''
index()方法传入一个值，值在列表中就返回它的下标，没有就报ValueError,
重复值，就返回第一次出现的下标
'''
print(lst.index(3))

'''
append()将元素添加到尾部
'''
lst.append("new")
print(lst)

'''
insert()将元素添加到列表指定位置
'''
lst.insert(1,"new two")
print(lst)

'''
remove()将传入的元素从列表中删除，元素不在列表中报ValueError
'''
lst.remove("new two")
print(lst)

#知道待删元素下标，del 删除
del lst[0]
print(lst)

'''
sort()对列表排序
注意：
sort()当场对列表排序，无需lst=lst.sort(reverse=False)这样编码
既有数字，又有字符的无法排序
字符是按ascii码排序
如果是字符，按字母顺序排序，可以使用参数lst.sort(key=str.lower)

'''
mylst=["apple","banana","orange","BBB"]
mylst.sort()
print(mylst)

mylst=["apple","banana","orange","BBB"]
mylst.sort(key=str.lower)
print(mylst)
