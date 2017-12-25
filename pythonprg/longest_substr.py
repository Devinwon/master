'''
求出一个字符串中最长回文字串
str='abcdzdcab'
返回cdzdc
abcdzdcab
abcdzdcab
'''
def isRevel(str):
	flag=True
	for index in range(len(str)//2+1):
		if index<=len(str)-index-1:
			if str[index]!=str[len(str)-index-1]:
				flag=False
				break
	return flag

str='abcdzdcab123454321ab123454321'
str_len=len(str)
rel=[]
for L in range(str_len-2):
	for M in range(L+2,str_len+1):
		if isRevel(str[L:M]):
			if len(rel)==0:
				rel.append(str[L:M])
				# print('fisrt',rel)
			else:
				# print('com1',str[L:M],len(rel[0]))
				if len(str[L:M])>len(rel[0]):
					# print('com2',str[L:M])
					rel[0]=str[L:M]
				elif len(str[L:M])==len(rel[0]):
					rel.append(str[L:M])
	
print('longest subString:',rel)
