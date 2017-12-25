n=input("请输入整数N: ")
sum=0
#range(),默认开始位置为0，步长为1
#注意冒号
for i in range(int(n)):
    sum+=i+1
    #print("1-",int(n),"的和为：",sum)

print("1-",int(n),"的和为：",sum)
