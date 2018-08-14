'''
Assume s is a string of lower case characters.

Write a program that prints the number of times the string 'bob' occurs in s. 
For example, if s = 'azcbobobegghakl', then your program should print

Number of times bob occurs is: 2
'''
cnt=0
src="bob"
s="azcbobobegghakl"
while True:
	if src in s:
		cnt+=1
		index=s.index(src)
		s=s[:index]+s[index+2:]
	else:
		break
print("Number of times bob occurs is: %d"%cnt)