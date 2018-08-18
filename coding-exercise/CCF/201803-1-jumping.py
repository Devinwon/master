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