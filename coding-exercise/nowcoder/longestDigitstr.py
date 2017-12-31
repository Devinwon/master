
'''
1个测试用例，
一个字符串str，长度不超过255。
abcd12345ed125ss123456789
123456789
'''
# str=input()
str='shjahdjjfsdjfksdjfksjkldkclsdk0-0-0-012'
# str='123a123a457'
# str='837147'
# str=''
# str='abcd12345ed125ss123456789'
rel=[]
if str.isdigit():
	rel.append(str)
elif str.isalpha():
	rel.append('')
else:
	for i in range(len(str)):
		if str[i].isalpha():
			continue
		else:
			for j in range(i+1,len(str)+1):
				substr=str[i:j]
				if substr.isdigit():
					if len(rel)==0:
						# 首元素插入不比较
						rel.append(substr)
						# print(rel[0])
					else:
						# 后续元素需要比较
						if len(rel[-1])==len(substr):
							# print(substr)
							rel.append(substr)
						elif len(rel[-1])<len(substr):
							# 更长的替换
							rel=['']
							rel[-1]=substr

				else:
					pass

for i in rel:
	print(i)
			


