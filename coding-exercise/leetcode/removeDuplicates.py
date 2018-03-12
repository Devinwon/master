'''
给定一个有序数组，你需要原地删除其中的重复内容，使每个元素只出现一次,并返回新的长度。
不要另外定义一个数组，您必须通过用 O(1) 额外内存原地修改输入的数组来做到这一点。


示例：
给定数组: nums = [1,1,2],
你的函数应该返回新长度 2, 并且原数组nums的前两个元素必须是1和2
不需要理会新的数组长度后面的元素

"""
:type nums: List[int]
:rtype: int
"""
'''
'''
class Solution:
	def removeDuplicates(self, nums):
		start=0
		while start<len(nums):
			if nums.count(nums[start])>1:
				dump_pop=nums[start]
				dump_cnt=nums.count(nums[start])
				for cnt in range(dump_cnt-1):
					nums.remove(dump_pop)
			else:
				start+=1
		# print(nums)
		return len(nums)
'''
class Solution:
	def removeDuplicates(self, nums):
		start=0
		for v in nums:
			if nums.count(v)>1:
				dump_pop=v
				dump_cnt=nums.count(v)
				for cnt in range(dump_cnt-1):
					nums.remove(dump_pop)
		print(nums)
		return len(nums)

s=Solution()
print(s.removeDuplicates([1,1,2,2,3,0,10,12,8,9,0,112,4,5,]))