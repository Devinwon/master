# Paste your code into this box 
sub=''
longsub=''
while len(longsub)<len(s) and s :
	sub=''
	gap=True
	for index in range(len(s)-1):
		if s[index]<=s[index+1]:
			sub+=s[index]
		else:
			sub+=s[index]
			s=s[index+1:]
			if len(sub)>len(longsub):
				longsub=sub
			# print(longsub,s)
			gap=False
			break
	if gap:
		if len(s)>len(longsub):
			longsub=s
		break
print("Longest substring in alphabetical order is: %s"%longsub)