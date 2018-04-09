cnt=int(input())
while cnt:
	cnt-=1
	num=int(input())
	if num%2!=0:
		print('No')
	else:
		for i in range(2,num):
			if (num%i)==0 and i%2==0 and (num%i)%2==0:
				print(num//i,i)
				break
		if i>=num:
			print('No')


