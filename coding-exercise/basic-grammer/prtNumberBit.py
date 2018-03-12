# 求出一共不大于5为的数字时几位数，
# 并且逆向输出每一位数字
n=int(input("Input a number(<=99999):"))
bit=0
for i in range(1,10):
    if(1<=n/(10**i)<=9):
        bit=i+1
        print("This number with",bit,"bit")
temp=n
for b in range(1,bit+1):
    print(temp%10,end='')
    temp=temp//10
print("")
