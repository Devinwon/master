'''
输入3个正数，判定它们作为三条边的边长能否组成一个三角形，
如果能，进一步判断三角形的形状（按等边、等腰、直角、一般的顺序），输出判断结果。
'''
print('输入三个正数：')
a=eval(input('a='))
b=eval(input('b='))
c=eval(input('c='))

# 构成三角形边的判断
if a+b>c and a+c>b and b+c>a:
	if a==b==c:
		print('构成一个等边三角形')
	elif a-b==0 or a-c==0 or b-c==0:
		print('构成一个等腰三角形')
	elif max(a,b,c)**2==((a+b+c)-max(a,b,c)-min(a,b,c))**2+min(a,b,c)**2:
		print('构成直角三角形')
	else:
		print('构成一般三角形')
else:
	print('不能构成三角形')