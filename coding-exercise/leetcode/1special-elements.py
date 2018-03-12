'''
给定一个整数数列，找出其中和为特定值的那两个数。
你可以假设每个输入都只会有一种答案，同样的元素不能被重用。

example

给定 nums = [2, 7, 11, 15], target = 9
因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]

'''

class Solution:
	def twoSum(self,nums, target):
		numsbak=nums[::]
		numsbak.sort()
		for i in range(len(numsbak)-1):
			if numsbak[i]+numsbak[-1]<target:
				continue
			else:
				for j in range(i+1,len(numsbak)):
					if numsbak[i]+numsbak[j]==target:
						if numsbak[i]==numsbak[j]:
							t=nums.index(numsbak[i])
							t2=nums.index(numsbak[j],t+1)
							rel=[t,t2]
						else:
							rel=[nums.index(numsbak[i]),nums.index(numsbak[j])]
						rel.sort()
						return rel
				

s=Solution()

print(s.twoSum([3,3,4],6))


# 还需要改进
		