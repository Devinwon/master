'''
title:
字符个数统计

题目描述
编写一个函数，计算字符串中含有的不同字符的个数。字符在ACSII码范围内(0~127)。
不在范围内的不作统计。

输入描述:
输入N个字符，字符在ACSII码范围内。

输出描述:
输出范围在(0~127)字符的个数。

case1:
Input:
abc

Output:
3
'''


from collections import Counter

asciistr=input()
cnt_dict=dict(Counter(asciistr))
rel=0
for k in cnt_dict.keys():
	if 0<=ord(k)<=127:
		rel+=1
print(rel)