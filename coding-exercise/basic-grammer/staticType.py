# 要求：输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数。
str=input("input something:")
alpha_cnt=0
digit_cnt=0
gap_cnt=0
other_cnt=0
lenofstr=len(str);
for x in range(lenofstr):
    if(str[x].isalpha()):
        alpha_cnt+=1
    elif(str[x].isdigit()):
        digit_cnt+=1
    elif(str[x].isspace()):
        gap_cnt+=1
    else:
        other_cnt+=1
print("alpha:",alpha_cnt)
print("digit:",digit_cnt)
print("gap:",gap_cnt)
print("other:",other_cnt)
