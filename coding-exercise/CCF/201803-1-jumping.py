"""
输入包含多个数字，用空格分隔，每个数字都是1，2，0之一，
1表示此次跳跃跳到了方块上但是没有跳到中心，
2表示此次跳跃跳到了方块上并且跳到了方块中心，
0表示此次跳跃没有跳到方块上（此时游戏结束）。

解题思路:
由于需要上一跳的得分,故而需要重新将每次得分保存下来

1 1 2 2 2 1 1 2 2 0
22
"""
score=[]							#每跳分数记录表
record=list(map(int,input().split()))
jumpCount=len(record) #跳跃次数


score.append(record[0])
if jumpCount>1:
	for val in record[1:]:
		if val!=2:
			score.append(val)
		else:
			# 跳到中心,并且不是第一跳,得分为2
			if score[-1]==1:
				score.append(2)
			else:
				score.append(2+score[-1])

# print(score)		
print(sum(score))