'''
title:
字符串最后一个单词的长度

#description:#
计算字符串最后一个单词的长度，单词以空格隔开。

###Input description###
一行字符串，非空，长度小于5000。

###Output description###
整数N，最后一个单词的长度。

#example#

###Input###
hello world

###Output###
5
'''

str = input().strip().split()
print(len(str[len(str)-1]))