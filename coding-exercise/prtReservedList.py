# prtReservedList.py
# 反向输出列表的元素
lst=['abc','1233','hahah',"XOXO"]
# for e  in range(len(lst)):
#     print(lst[len(lst)-(e+1)])

for e in lst[::-1]:
    print(e)
print(lst)
