# 将字符串中的空格以20%替换
# 'abc 123 irui   82389'
str='abc 123 irui   82389'

# 方法1
# gapnum=str.count(' ')
# print(gapnum)
# str=str.split(' ')
# temp='20%'
# rel=''
# for item in str:
# 	rel=rel+item+temp

# rel=rel[:-3]
# print(rel)

# 方法2
temp='20%'
rel=''
for i in str:
	if i==' ':
		rel=rel+temp
	else:
		rel=rel+i
print(rel)
	# print(i,end='',sep='')

t1= "I'm %(nickname)s. My real name is %(name)s, but my friends call me %(nickname)s."
def r(name, nickname):
		return t1 %{'name':name,'nickname':nickname}
print(r("Mike", "Goose"))