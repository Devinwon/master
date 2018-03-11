'''
给定一个范围为 32 位 int 的整数，将其颠倒。

case1:
输入: 123
输出:  321

case2:
输入: -123
输出: -321

case3:
输入: 120
输出: 21

注意:

假设我们的环境只能处理 32 位 int 范围内的整数。
根据这个假设，如果颠倒后的结果超过这个范围，则返回 0。
"""
:type x: int
:rtype: int
"""

32位整数中-2147483648到2147483647
'''

class Solution:
	def reverse(self, x):
		if x<0:
			signal=-1
		elif x>0:
			signal=1
		else:
			signal=0
		x=str(abs(x))[::-1]
		while len(x) and x!='0':
			if x[0]=='0':
				x=x[1:]
			else:
				break
		x=signal*int(x)
		if -2**31-1<=x<=2**31:
			return x
		else:
			return 0

s=Solution()
print(s.reverse(0))
print(s.reverse(-123))
print(s.reverse(120))
print(s.reverse(2147483647))
print(s.reverse(-2147483647))



