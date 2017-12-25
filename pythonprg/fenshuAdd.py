a1=2
b1=1

x1=3
y1=2

sum=a1/b1+x1/y1
for i in range(3,21):
    z1=x1
    z2=y1
    x1=x1+a1
    y1=y1+b1
    a1=z1
    b1=z2
    sum+=(x1)/(y1)
print(sum)
