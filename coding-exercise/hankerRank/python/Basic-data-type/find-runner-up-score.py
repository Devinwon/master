"""
https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem
"""

if __name__ == '__main__':
	n = int(input())
	arr = map(int, input().split())
	# 必须先转换成list,如果先转成集合是空的集合
	arr_set=set(list(arr))
	if len(arr_set)>=2:
		print(sorted(list(arr_set))[-2])
