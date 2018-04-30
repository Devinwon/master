
dic = {'data5':10,'data1':3, 'data2':1, 'data3':2, 'data4':4}

print('将键名提取出来排序\n',sorted(dic.keys()),sep='')
# sorted(dic)等同于sorted(dic.keys())
# print('将值提取出来排序\n',sorted(d.values()),sep='')
# print('按键进行排序\n',sorted(dic.items()),sep='')


# 对字典的值进行排序的三种方法:

# 方法1
"""
print(sorted(dic.items(),key = lambda x:x[1]))
print(sorted(dic.items(),key = lambda x:x[0]))
"""

# 方法2
"""
from operator import itemgetter
print(sorted(dic.items(),key = itemgetter(1)))
"""

# 方法3
"""
print(sorted(zip(dic.values(),dic.keys())))
"""