'''
根据 a,b 的假设三种（1，0），（0，1），（1，1）
'''
for a,b in ((1,0),(0,1),(1,1)):
    # print(a,b)
    # print(type(a))
    # if a,b=1,0:        #假设a,b（0，1），（1，1）
    c=b             #求解c
    d=abs(c-1)      #求解d

    #验证
    if a+d==0 or a+d==1:
        pass
    else:
        continue

    if d==0:
        e=0         #求解e

    #验证：
    f=2-a-e
    if f<=1:
        print(a,b,c,d,e,f)
    else:
        continue

