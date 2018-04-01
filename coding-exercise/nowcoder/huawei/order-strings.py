'''
title:
字串的连接最长路径查找

#description:#
给定n个字符串，请对n个字符串按照字典序排列。

###Input description###
输入第一行为一个正整数n(1≤n≤1000),下面n行为n个字符串(字符串长度≤100),
字符串中只含有大小写字母。

###Output description###
数据输出n行，输出结果为按照字典序排列的字符串。

#example#

###Input###
9
cap
to
cat
card
two
too
up
boat
boot

###Output###
boat
boot
cap
card
cat
to
too
two
up
'''


cnt=int(input())
rel=[]
for i in range(cnt):
	rel.append(input())

rel.sort()

for v in rel:
	print(v)
