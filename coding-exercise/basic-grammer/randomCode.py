'''
implement random code for login or registe

'''
import random
char_set=list(range(65,91))
int_set=list(range(0,10))
rel_set=char_set+int_set

rel_str=''
code_bit=4
cnt=0
while cnt<code_bit:
	num=random.choice(rel_set)
	if num>10:
		c=chr(num)
	else:
		c=str(num)
	rel_str+=	c
	cnt+=1
print(rel_str)