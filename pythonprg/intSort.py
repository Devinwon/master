cnt=int(input("input the no of element:"))
ilist=[0]*cnt
for i in range(cnt):
    ilist[i]=int(input("input goal element:"))
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
