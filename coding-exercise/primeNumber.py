# 101-200之间的素数统计并输出
def isprime(n):
    res=1
    for i in range(2,int(n/2)+1):
        if(n%i==0):
            res=0
            break
    return res
cnt=0
for i in range(101,200):
    if(isprime(i)):
        cnt+=1
        print(i,end=' ')
        if(cnt%5==0):
            print('\n')
print("\nTotal primes:",cnt)
