"""
https://www.hackerrank.com/challenges/nested-list/problem

"""

if __name__ == '__main__':
	stuMarks=[]
	for _ in range(int(input())):
		name = input()
		score = float(input())
		stuMarks.append([name,score])
	# 按分数降序序
	stuMarks.sort(key=lambda x:(x[1]))
	# print(stuMarks)
	relName=[]
	relScore=0
	for i in range(1,len(stuMarks)):
		if not relName:
			# 还没有找到次小的成绩
			if stuMarks[i][1]>stuMarks[0][1]:
				relName.append(stuMarks[i][0])
				# 存储次小成绩
				relScore=stuMarks[i][1]
		else:
			# 已经找到次小的成绩,
			if stuMarks[i][1]==relScore:
				relName.append(stuMarks[i][0])
			else:
				break
	relName.sort()
	print('\n'.join(relName))
