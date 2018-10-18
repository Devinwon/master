# coding:utf-8
"""
问题描述
　　有 N 个非零且各不相同的整数。请你编一个程序求出它们中有多少对相反数(a 和 -a 为一对相反数)。
输入格式
　　第一行包含一个正整数 N。(1 ≤ N ≤ 500)。
　　第二行为 N 个用单个空格隔开的非零整数,每个数的绝对值不超过1000,保证这些整数各不相同。
输出格式
　　只输出一个整数,即这 N 个数中包含多少对相反数。
样例输入
5
1 2 3 -1 -2
样例输出
2


没有重复的数字，显然，求出比0下，

查看有没有比相反数字
"""
n=int(input().strip())
nlst=list(map(int,input().strip().split()))
nlst.sort()
cnt=0
start=0

# 注意条件的先后顺序，避免索引超出范围
while start<n and  nlst[start]<0:
	if -nlst[start] in nlst:
		cnt+=1
	start+=1

print(cnt)

