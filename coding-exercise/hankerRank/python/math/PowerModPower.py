'''
https://www.hackerrank.com/challenges/python-power-mod-power/problem
'''
a=eval(input().strip())
b=eval(input().strip())
m=eval(input().strip())
rel=a
for _ in range(abs(b)-1):
	rel*=a

if b<0:
	rel=1/rel
print(rel)
print(rel%m)
