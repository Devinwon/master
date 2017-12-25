# -*- coding: utf-8 -*-
'''
查找一个给定（1-1000000）元素是否为fibonacci元素，
如果不是，给出需要变换的最少步数，你可以每次+1或者-1进行变换
'''
# def Fibo(n):
#     if n>=0 and n<2:
#         return n
#     else:
#         return Fibo(n-1)+Fibo(n-2)
# 解题关键，使用递归太耗资源了，可以直接将列表构造出，总共32个
# 构造列表的方式也要注意，不要递归，直接将列表末尾元素相加后添加到原列表尾部
# 这一步是关键，否则继续递归占内存，然后循环比较即可
# all 32 items

import math
fibo_list=[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144,\
            233, 377, 610, 987, 1597, 2584, 4181, 6765,\
             10946, 17711, 28657, 46368,75025, 121393,\
             196418, 317811, 514229, 832040, 1346269]

N=int(input())

for index in range(32):
    if (abs(N-fibo_list[index]))<abs(N-(fibo_list[index+1])):
        print(abs(N-fibo_list[index]))
        break
    

