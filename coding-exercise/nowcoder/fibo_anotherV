def fibo(n):
	rel=0
	if n==1:
		rel=1
	elif n>1:
		lst=[0,1]
		for i in range(2,n+1):
			t=i**3+i**2+i+1+lst[i-1]+lst[i-2]
			lst.append(t)
		rel=lst[-1]
	return rel%(10**9+7)

cnt=int(input())
for _ in range(cnt):
	num=int(input())
	print(fibo(num))
