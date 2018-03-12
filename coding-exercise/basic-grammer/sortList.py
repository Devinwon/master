ilist=[20,44,-34,10,88,99,0,1000,-99]
print("Before",ilist)

# from small to large
# 冒泡排序1
# for i in range(len(ilist)-1):
#     for j in range(i+1,len(ilist)):
#         if(ilist[i]>ilist[j]):
#             temp=ilist[i]
#             ilist[i]=ilist[j]
#             ilist[j]=temp

# 下标索引排序
lenoflist=len(ilist)
for j in range(lenoflist):
    maxindex=0
    for i in range(lenoflist-j):
        if(ilist[i]>ilist[maxindex]):
            maxindex=i
    if(maxindex!=lenoflist-1-j ):
        # 注意什么情况需要交换，不能简单的认为是首元素
        # 本次maxindex不是倒数对应j位置就需要交换
        # 理想情况maxindex所处位置与(第j次循环的)倒数j位置重合，就不需要交换 ，
        temp=ilist[-(j+1)]
        ilist[-(j+1)]=ilist[maxindex]
        ilist[maxindex]=temp
    # print(j,"turn",ilist)

print("After:",ilist)
