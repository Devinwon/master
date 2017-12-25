'''
Assume s is a string of lower case characters.

Write a program that prints the longest substring of s in which the letters occur in alphabetical order. 
For example, if s = 'azcbobobegghakl', then your program should print
Longest substring in alphabetical order is: beggh

In the case of ties, print the first substring. 
For example, if s = 'abcbcd', then your program should print

Longest substring in alphabetical order is: abc

记录字串
顺序遍历
'''
sub=''
longsub=''
# s = 'aaaaaaagzzzz'
s = 'azcbobobegghakl'
# s='abcbcd'
# orilen=len(s)

# 这里的判断改进
while len(longsub)<len(s) and s :
	sub=''
	for index in range(len(s)-1):
		if s[index]<=s[index+1]:
			sub+=s[index]
		else:
			sub+=s[index]
			s=s[index+1:]
			if len(sub)>len(longsub):
				longsub=sub
			# print(longsub,s)
			break
print("Longest substring in alphabetical order is: %s"%longsub)