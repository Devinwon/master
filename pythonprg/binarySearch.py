lst=[12,3,4,5,6,7,89,0,675,342,34,55,67,78,90]
list.sort(lst)
print(lst)
key=int(input("Input the search number:"))

# binary search log2N效率
def binSea(obj,key):
    lenofobj=len(obj)
    right=0
    left=lenofobj-1
    res=0
    index=0
    while(right<=left):
        mid=(right+left)//2
        if(key<obj[mid]):
            left=mid-1
        elif(key>obj[mid]):
            right=mid+1
        else:
            res=1
            index=mid
            break
    if(res):
        print("Found in %d in lst"%(index+1))
    else:
        print("NOT Found")

binSea(lst,key)

# def stepbystepSea(obj,key):
#     res=0
#     for e in obj:
#         if(e==key):
#             res=1
#             break
#     if(res):
#         print("Found")
#     else:
#         print("Not found")
# stepbystepSea(lst,key)
