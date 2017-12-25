# a=input("Input number:")
# if(a):
#     print(a)
# else:
#     print("Nothing")

# 构造一个列表，
sortList=[]
temp=1
while(1):
    temp=input("Input number:")
    # 无法输入负数
    if(temp.isdigit()):
        sortList.append(int(temp))
    else:
        break
print("Original list:",sortList)
# 排序后输出最大最小的数据
list.sort(sortList)
print("Ordered list:",sortList)
print(sortList)
if(len(sortList)>1):
    print("min:",sortList[0])
    print("max:",sortList[-1])
else:
    print("only one element:",sortList[0])

# get max number in three
# if(a>b):
#     temp=a
# else:
#     temp=b
#
# if(c>temp):
#     print("Max number in three is:",c)
# else:
#     print("Max number in three is:",temp)
