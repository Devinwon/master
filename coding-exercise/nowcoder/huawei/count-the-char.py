'''
title:
计算字符个数

#description:#
写出一个程序，接受一个有字母和数字以及空格组成的字符串，
和一个字符，然后输出输入字符串中含有该字符的个数。
不区分大小写。

###Input description###
输入一个有字母和数字以及空格组成的字符串，和一个字符。

###Output description###
输出输入字符串中含有该字符的个数。

#example#

###Input###
ABCDEF A

###Output###
1
'''

s=input()
c=input()
s=s.upper()
c=c.upper()
print(s.count(c))