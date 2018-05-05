"""
https://www.hackerrank.com/challenges/kangaroo/problem
"""
#!/bin/python3

import sys

def kangaroo(x1, v1, x2, v2):
	# Complete this function
	# return YES OR NO
	jump=0
	rel='NO'
	while jump<=10000:
		s1=x1+(jump*v1)
		s2=x2+(jump*v2)
		if s1==s2:
			rel='YES'
			break
		print('s1=',s1,'_','s2=',s2)
		jump+=1
	return rel

x1, v1, x2, v2 = input().strip().split(' ')
x1, v1, x2, v2 = [int(x1), int(v1), int(x2), int(v2)]
result = kangaroo(x1, v1, x2, v2)
print(result)