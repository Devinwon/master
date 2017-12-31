print("---Here is testing your input---")
# how to judge input  contains alpha and digit or others
# 估计需要正则表达式的使用
temp=input("input something:")
if(temp.isdigit()):
    print("input is digital:",temp)
elif(temp.isalpha()):
    if(temp.islower()):
        print("input is lower alpha:",temp)
    elif(temp.isupper()):
        print("input is upper alpha:",temp)
    else:
        print("input is lower mixed upper alpha:",temp)
else:
    print("input is neither alpha nor digit alpha:",temp)
