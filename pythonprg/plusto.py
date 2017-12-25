def plusto(f):
    if(f==0):
        sum= 1
    else:
        sum=plusto(f-1)*f
    return sum

sum=0
for i  in range(1,8):
    sum+=plusto(i)
print(sum)
