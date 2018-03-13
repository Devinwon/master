'''
35. 搜索插入位置
给定一个排序数组和一个目标值，如果在数组中找到目标值则返回索引。
如果没有，返回到它将会被按顺序插入的位置。
你可以假设在数组中无重复元素。


case1:
输入: [1,3,5,6], 5
输出: 2

case2:
输入: [1,3,5,6], 2
输出: 1

case3
输入: [1,3,5,6], 7
输出: 4

case4
输入: [1,3,5,6], 0
输出: 0

'''
"""
:type nums: List[int]
:type target: int
:rtype: int
"""

class Solution:
	def searchInsert(self, nums, target):
		if nums.count(target):
			return nums.index(target)
		else:
			if target<nums[0]:
				return 0
			elif target>nums[-1]:
				return len(nums)
			else:
				for i in range(len(nums)):
					if nums[i] <target<nums[i+1]:
						return i+1

'''
if target<nums[0]:
	return 0
elif target>nums[-1]:
	return len(nums)
else:
	for v in nums:
		if v <target:
			return nums[v]+1
'''


'''
class Solution:
	def searchInsert(self, nums, target):
		if nums.count(target):
			return nums.index(target)
		else:
			nums.append(target)
			nums.sort()
			return nums.index(target)

'''

s=Solution()
print(s.searchInsert([1,3,5],4))

