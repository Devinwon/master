'''
n = 11，m = 4，按字典序排列依次为1, 10, 11, 2, 3, 4, 5, 6, 7, 8, 9，因此第4个数字为2。
'''
getnm=list(input().split())
n=int(getnm[0])
m=int(getnm[1])

if m<=n:
	strlist=[]
	for i in range(1,n+1):
		strlist.append(str(i))

	print(strlist)
	strlist.sort()
	print(strlist)
	print(strlist[m-1])
else:
	print('')

