N=input("输入待求阶乘N：")
sum,temp=0,1


for i in range(1,int(N)+1):
    temp*=i
    sum+=temp
print("运算结果是：{}".format(sum))
