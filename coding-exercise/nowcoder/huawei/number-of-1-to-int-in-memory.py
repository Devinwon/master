'''
#description:#
输入一个int型的正整数，计算出该int型数据在内存中存储时1的个数。

###Input description###
输入一个整数（int类型）

###Output description###
这个数转换成2进制后，输出1的个数

#example#

###Input###
5

###Output###
2
'''

i=int(input())
print(bin(i).count('1'))