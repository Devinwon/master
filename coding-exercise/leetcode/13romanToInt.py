'''
13. 罗马数字转整数

给定一个罗马数字，将其转换成整数。
返回的结果要求在 1 到 3999 的范围内。
小大  -   小的数字限于（I X V）
大小  +
'''


"""
:type s: str
:rtype: int
"""

class Solution:
	def romanToInt(self, s):
		roma_dict={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
		intnumber=0
		while s :
			if len(s)>=2:
				if roma_dict[s[0]] <roma_dict[s[1]]:
					intnumber+=roma_dict[s[1]]-roma_dict[s[0]]
					s=s[2:]
				else:
					intnumber+=roma_dict[s[0]]
					s=s[1:]
			elif len(s)==1:
				intnumber+=roma_dict[s[0]]
				s=s[1:]
		return intnumber

s=Solution()
print(s.romanToInt('CD'))
print(s.romanToInt('CMXCIX'))
print(s.romanToInt('VI'))
print(s.romanToInt('X'))
print(s.romanToInt('IX'))
print(s.romanToInt('XI'))
print(s.romanToInt('XXIX'))
print(s.romanToInt('MMMCMXCIX'))