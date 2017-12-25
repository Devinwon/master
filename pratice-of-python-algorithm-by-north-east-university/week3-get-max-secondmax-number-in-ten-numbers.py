'''
输入十个不同的数字，
输出其中最大的数和次大的数。
例如输入1，3，5，7，9，2，4，6，8，10，
输出：最大的数是10，次大的数是9.

读题：相等就输出一个
次大：小于最大，差值最小
'''

# 如果有多个最大最小，程序只输出一个结果
# 输入的数据都一样大，程序认为没有次大的数


imax=eval(input())
cnt=10-1
numlst=[]
numlst.append(imax)
while cnt:
	t=eval(input())
	numlst.append(t)
	if imax<t:
		imax=t
	cnt-=1
print("输入的最大数为:",imax)

diff=0
for v in numlst:
	if v<imax:
		d=imax-v
		if diff==0:
			diff=d
		if diff>d:
			diff=d
if diff:
	print("输入的次大数为:",imax-diff)
else:
	print("没有次大的数，都一样大")