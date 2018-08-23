"""
问题描述

　　给定n个正整数，找出它们中出现次数最多的数。如果这样的数有多个，请输出其中最小的一个。

输入格式

　　输入的第一行只有一个正整数n(1 ≤ n ≤ 1000)，表示数字的个数。
 　　输入的第二行有n个整数s1, s2, …, sn (1 ≤ si ≤ 10000, 1 ≤ i ≤ n)。相邻的数用空格分隔。

输出格式

　　输出这n个次数中出现次数最多的数。如果这样的数有多个，输出其中最小的一个。

样例输入

6
 10 1 10 20 30 20

样例输出

10

1:对数据进行基本的处理
2:将数据结构改为集合,去掉重复元素并排序,然后集合中统计每个元素的出现系数,
	分别使用变量进行保存,以便进行比较,多个取最小的,所以不包括=情况(已经排序)

"""
Numcount=int(input().strip())
numlst=list(map(int,input().strip().split()))
numset=list(set(numlst))
numset.sort()

# record the result
cnt=1
num=numset[0]


for v in numset[1:]:
	t=numlst.count(v)
	if t>cnt:			#已近排序了,只存储最大的即可
		cnt=t
		num=v
print(num)

