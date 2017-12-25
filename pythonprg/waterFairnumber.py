# 一位数都是水仙花数
#两位数呢
# i代表是几位数
cnt=0
for i in range(1,5):
    if(i==1):
        for j in range(1,10):
            if(j**i==j):
                cnt+=1
                if (cnt%5==0) :
                    print(j)
                else:
                    print(j," ",end='')

    elif(i==2):
        for j in range(10,100):
            a=j//10
            b=j%10
            if(a**i+b**i==j):
                cnt+=1
                if (cnt%5==0):
                    print(j)
                else:
                    print(j," ",end='')

    elif(i==3):
        for j in range(100,1000):
            a=j//100
            b=j//10%10
            c=j%10
            # print(j,":",a,b,c)
            if(a**i+b**i+c**i==j):
                cnt+=1
                if(cnt%5==0):
                    print(j)
                else:
                    print(j," ",end='')

    elif(i==4):
        for j in range(1000,10000):
            a=j//1000
            b=j//100%10
            c=j//10%10
            d=j%10
            # print(j,":",a,b,c)
            if(a**i+b**i+c**i+d**i==j):
                cnt+=1
                if cnt%5==0 :
                    print(j)
                else:
                    print(j," ",end='')
