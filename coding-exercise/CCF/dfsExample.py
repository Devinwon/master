"""
深度优先搜索
模拟数字1-9的排列情况
"""

n=2
#初始化
book=[0 for _ in range(n)]	#记录数字使用情况

ret=[0 for _ in range(n)]		#记录结果

def dfs(step):
	if step==n+1:
		# 表示所有的数字都已经用完了
		# 打印排列结果
		for i in range(n):
			print(ret[i],end='')
		print()
		return 
	for i in range(n):
		if book[i]==0:
			ret[step-1]= i+1
			book[i]=1
			dfs(step+1)
			book[i]=0
dfs(1)	