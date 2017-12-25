# 判断一个5位数是不是回文数，如12321就是，逆序正序都时一样就是
n=input("Input a number with 5 bit:")
lenofn=len(n)
flag=1
for i in range(0,lenofn//2):
    if(n[i]!=n[lenofn-(i+1)]):
        flag=0
        break
if(flag):
    print("OK")
else:
    print("NO")
