'''
title:
质数因子

#description:#
输入一个正整数，按照从小到大的顺序输出它的所有质数的因子
（如180的质数因子为2 2 3 3 5 ）
最后一个数后面也要有空格

###Input description###
输入一个long型整数

###Output description###
按照从小到大的顺序输出它的所有质数的因子，以空格隔开。最后一个数后面也要有空格。

#example#

###Input###
180

###Output###
2 2 3 3 5 
'''

import math
i=int(input())

'''

def isprime(n):
	flag=True
	for i in range(2,int(math.sqrt(n))+1):
		if n%i==0:
			flag=False
			break
	return flag

def factorOf(n):
	if isprime(n):
		print(n,' ',sep='',end='')
	else:
		start=2
		while start<=int(math.sqrt(n))+1 :
			if n%start==0 and isprime(start):
				print(start,' ',sep='',end='')
				factorOf(n//start)
				break
			start+=1
'''
def factorOf(n):
	while n!=1:
		start=2
		while start<=n:
			if n%start==0:
				print(start,' ',sep='',end='')
				break
			start+=1
		n//=start

factorOf(i)


# 每次从2开始，不需要判断除数是否为 质数，因为每次从2开始除数不可能为合数

#如果不检查输入的数是否为质数，则要一直遍历到n(这个数本身) 






