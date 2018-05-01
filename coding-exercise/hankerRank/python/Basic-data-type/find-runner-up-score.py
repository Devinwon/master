"""
https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem
"""

if __name__ == '__main__':
	n = int(input())
	arr = map(int, input().split())
	arr_set=set(list(arr))
	if len(arr_set)>=2:
		print(sorted(list(arr_set))[-2])
