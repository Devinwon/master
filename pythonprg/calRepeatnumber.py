# 求这样的一组数据和，s=a+aa+aaa+aaaa+aa...a的值，其中a是一个数字；
# 例如：2+22+222+2222+22222(此时共有5个数相加)，这里具体是由几个数相加，由键盘控制
#常见的构造列表存储方法，然后再进行计算
singleNum=int(input("input only one number(1-9):"))
maxbit=int(input("input max bit:"))
sum=0
for i in range(1,maxbit+1):
    for j in range(1,i+1):
        temp=singleNum*(10**(j-1))
        sum+=temp
print(sum)
