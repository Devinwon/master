'''
实现 strStr()。

返回蕴含在 haystack 中的 needle 的第一个字符的索引，
如果 needle 不是 haystack 的一部分则返回 -1 。

case1:
输入: haystack = "hello", needle = "ll"
输出: 2

case2:
输入: haystack = "aaaaa", needle = "bba"
输出: -1


多思考
'''

"""
:type haystack: str
:type needle: str
:rtype: int
"""
class Solution:
	def strStr(self, haystack, needle):
		return haystack.find(needle)