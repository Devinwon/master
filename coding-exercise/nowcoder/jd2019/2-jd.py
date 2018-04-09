s=input()

def rs(s):
	flag=True
	for i in range(len(s)//2):
		if s[i]!=s[-(i+1)]:
			flag=False
			break
	return flag

# print(rs('AB'))
cnt=len(s)
for i in range(2,len(s)+1):
	
