
'''
n级台阶，青蛙一次可以跳一阶或两阶
可以有多少种跳法
满足斐波数列
'''
# 使用循环效率较高
def spstatic(n):
	if n<=3:
		return n
	else:
		s2=2
		s3=3
		for x in range(4,n+1):
			t=s2+s3
			s2=s3
			s3=t
		return t

n=int(input())
print(spstatic(n))

# 递归效率不高问题
'''
def cnt(n):
	if n<=3:
		return n
	else:
		return cnt(n-2)+cnt(n-1)

n=int(input())
print(cnt(n))
'''