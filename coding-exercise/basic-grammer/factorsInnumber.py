'''
12=2*2*3的形式列出一个输入数的因子
不包含1与本身

'''

number=int(input("Input a number:"))
def isprime(n):
    res=1
    for i in range(2,int(n/2)+1):
        if(n%i==0):
            res=0
            break
    return res

if(isprime(number)):
    print(number,"=",number,sep='')
else:
    print(number,"=",sep='',end='')
    factor=2
    # 用2除，结果判断，更新number，对新numbers判断
    # 重复，不行就尝试下一个除数3，4，5
    # number不符合推出loop
    while( not isprime(number)):
        if(number%factor==0):
            print(factor,end='*')
            number=number//factor
        else:
            factor+=1
    print(number)
