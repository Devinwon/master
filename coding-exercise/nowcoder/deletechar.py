# str1=input()
str1="They are students."
# str2=input()
str2='aeiou'

'''
Thy r stdnts.
'''

for c in str2:
	while c in str1:
		# 只返回了满足条件的首个
		c_index=str1.index(c)
		str1=str1[:c_index]+(str1[c_index+1:])

print(str1)

# 或者使用str1.replace(c,""),将满足条件的全部替换为空'',效率更高