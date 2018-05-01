"""
https://www.hackerrank.com/challenges/finding-the-percentage/problem
"""
if __name__ == '__main__':
	n = int(input())
	student_marks = {}
	for _ in range(n):
		# 这个用法注意一下,之前都没有见过line是个列表,包含后面所有的元素
		# 有点类似参数的形式,不限个数
		name, *line = input().split()
		scores = list(map(float, line))
		student_marks[name] = scores
	# print(student_marks)
	query_name = input()
	print("{:.2f}".format((sum(student_marks[query_name])/3)))