'''
title:
提取不重复的整数

#description:#
输入一个int型整数，
按照从右向左的阅读顺序，
返回一个不含重复数字的新的整数。

###Input description###
输入一个int型整数

###Output description###
按照从右向左的阅读顺序，返回一个不含重复数字的新的整数

#example#

###Input###
9876673

###Output###
37689
'''

num=input()
rel=""
for v in num[::-1]:
	if v not in rel:
		rel+=v

print(rel)