'''
初始化如下列表
alist = [12, 34, 51, 66, 31, 7, 87, 58, 92]
从键盘输入一个整数。
如果该数是奇数，计算alist中所有奇数的和，并将该和值加到列表的末尾；
如果为偶数，则计算alist中所有偶数的和并加到列表末尾。
输出最终的alist。
'''
alist = [12, 34, 51, 66, 31, 7, 87, 58, 92]
try:
	num=int(input())
	sum_part=0
	if num%2==0:
		# num是偶数
		for v in alist:
			if v%2==0:
				sum_part+=v
	else:
		# num是奇数
		for v in alist:
			if v%2!=0:
				sum_part+=v
	alist.append(sum_part)
	print("最终的列表alist为\n",alist)

except:
	print("我们期望你输入一个整数")
