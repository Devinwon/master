# 计算两个数的和，然后格式化输出
 
'''
method 1
a,b=(input().split())
a=int(a)
b=int(b)

print(format(a+b,','))
'''

'''
method 2
'''
import math
a,b=(input().split())
c=int(a)+int(b)
c=str(c)

l=len(c)
if int(c)<0:
	l=l-1
	print('-',end='')

c=str(abs(int(c)))

if l<=3:
	print(c)
else:
	count=int(l/3)-1
	if l%3!=0:
		count=int(l/3)

	# 前置字串为l-count*3
	print(c[:l-count*3],end='')
	while count:
		start=l-count*3
		print(',',c[start:start+3],sep='',end='')
		count-=1
		start+=3



