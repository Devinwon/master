# 1、1、2、3、5、8、13、21、34
# get every element in Fibonacci sequence
def Fibo(n):
    if(n==1 or n==2):
        res=1
    elif(n<1):
        print("Error input")
        res=0
    else:
        res=Fibo(n-1)+Fibo(n-2)
    return res
# initinalize the Fibolist
Fibolist=[1]
sn=int(input("input sn:"))
if(sn>=2):
    for i in range(2,sn+1):
        # append element into Fibolist by loop
        Fibolist.append(Fibo(i))
        
# print the Fibonacci sequence
print(Fibolist)
