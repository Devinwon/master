# 1 2 3 4
# 能组成多少个互不相同的三位数
# 4*3*2=24
numbers=[1,2,3,4]
cnt=0
for i in numbers:
    for j in numbers:
        for k in numbers:
            if(i!=j and j!=k and i!=k):
                cnt=cnt+1
                print(cnt,":",i*100+j*10+k)
