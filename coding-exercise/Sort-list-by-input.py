'''
对用户随机输入的元素排序输出
'''

cnt=int(input("input the number of element:"))
ilist=[]
for i in range(cnt):
    ilist.append(int(input("input element:")))
print("The original sn:",ilist)
# ilist[len(ilist)]=int(input("new element:"))
# from small to large
list.sort(ilist)
# temp=0
# for j in range(3-1):
#     k=j+1
#     for k in range(3):
#         if(ilist[j]>ilist[j]):
#             temp=ilist[j]
#             ilist[j]=ilist[k]
#             ilist[k]=temp

print("The after sn:",ilist)
