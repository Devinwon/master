a=int(input("输入一个数"))
b=int(input("输入一个数"))
if b>=a:
    a,b=b,a
n=1
while n<=8:
    c=int(input("输入一个数"))
    if c>=a:
        b=a
        a=c
    elif c<=b:
        b
    else:
        b=c
    n=n+1
print("最大的数是%d"%a)
print("第二大的数是%d"%b)