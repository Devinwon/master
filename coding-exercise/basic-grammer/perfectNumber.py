# 它所有的真因子（即除了自身以外的约数）的和，恰好等于它本身。
# 如果一个数恰好等于它的因子之和，则称该数为“完全数”。
# 6=1+2+3满足条件
# 1000内所有的完数

# 分析：素数不是完数
start=6
end=10000

for i in range(start,end+1):
    sum=1
    factor=[]
    for j in range(2,int(i/2)+1):
        if(i%j==0):
            sum+=j
            factor.append(j)
    if(sum==i):
        print(i,'=1',sep='',end='')
        for e in factor:
            print('+',e,sep='',end='')
        print('\n')
