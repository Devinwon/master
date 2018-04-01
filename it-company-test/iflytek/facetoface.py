# L\R组成的字符串,'RL'
# 最少剩下多少人呢
'''
找到RL的起始位置，
如果前面为L，则删除L，剩下R
如果前面为R或者后面为L，则删除R，剩下L，构成RL
'''

# q=input()

q='LRRLRL'
cnt=len(q)
while 'RL' in q:
	index=q.index('RL')
	# 前后不一定存在
	try:

		if q[index-1]=='R' or q[index+2]=='L':
			q=q[:index]+q[index+1:]
		else:
			q=q[:index+1]+q[index+2:]
		cnt-=1
	except:
		pass

print(cnt)