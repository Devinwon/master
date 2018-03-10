'''
#description:#
•连续输入字符串，请按长度为8拆分每个字符串后输出到新的字符串数组； 
•长度不是8整数倍的字符串请在后面补数字0，空字符串不处理。 

###Input description###
连续输入字符串(输入2次,每个字符串长度小于100)

###Output description###
输出到长度为8的新字符串数组

#example#

###Input###
abc
123456789

###Output###
abc00000
12345678
90000000
'''
str1,str2=input(),input()
def string_split(s):
	if len(s)<=8:
		print("{:0<8}".format(s))
	else:
		print(s[:8])
		string_split(s[8:])
string_split(str1)
string_split(str2)
