'''
58. 最后一个单词的长度
给定一个字符串， 包含大小写字母、空格 ' '，请返回其最后一个单词的长度。
如果不存在最后一个单词，请返回 0 。
注意事项：一个单词的界定是，由字母组成，但不包含任何的空格。

case:
输入: "Hello World"
输出: 5
'''
"""
:type s: str
:rtype: int

多思考，不思考没有进步呀
"""
class Solution:
	def lengthOfLastWord(self, s):
		s=s.strip().split()
		return len(s[-1]) if s  else 0

s=Solution()
print(s.lengthOfLastWord('  123'))
print(s.lengthOfLastWord('  abc '))
print(s.lengthOfLastWord('  123 good  '))
print(s.lengthOfLastWord('    '))