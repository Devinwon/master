"""
:type x: int
:rtype: bool
"""
class Solution:
  def isPalindrome(self, x):
  	return str(x)==str(x)[::-1]