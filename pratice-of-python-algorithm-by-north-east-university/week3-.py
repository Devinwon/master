'''
用户输入的10个数进行排序，输出最大，次大数
没有考虑数据的相同
'''


a=[]
for h in range(10):
    x=int(input("input your number:"))
    a.append(x)
for i in range(len(a)-1):
    for j in range(len(a)-1-i):
        if a[j]>a[j+1]:
            a[j],a[j+1]=a[j+1],a[j]
print(a[-1],a[-2])