def cnt_bit(n):
	t=10
	cnt=0
	while True:
		if n//t==0:
			bitwide=len(str(t//10))
			cnt	+=bitwide*(n-t//10+1)
			break
		else:
			bitwide=len(str(t//10))
			cnt	+=bitwide*(t-1)*(t//10)
			t=t*10
	return cnt


cnt=int(raw_input())
for n in range(cnt):
	num=int(raw_input())
	print(cnt_bit(num))