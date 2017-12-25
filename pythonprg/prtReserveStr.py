str=input("Input something:")
# for e in range(len(str)-1,-1,-1):
#     print(str[e])

# 递归函数调用的方式反向输出字符
def reserveStr(s):
    if(len(s)>1):
        print(s[-1])
        temp=s[:-1]
        reserveStr(temp)
    else:
        print(s[0])

reserveStr(str)
