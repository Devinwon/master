'''
running with python3

'''
# def cnt_bit(n):
# 	t=10
# 	cnt=0
# 	while True:
# 		if n//t==0:
# 			bitwide=len(str(t//10))
# 			cnt	+=bitwide*(n-t//10+1)
# 			break
# 		else:
# 			bitwide=len(str(t//10))
# 			cnt	+=bitwide*(t-1)*(t//10)
# 			t=t*10
# 	return cnt


cnt=int(input())
# 数据个数
for n in range(cnt):
	bitwide=0
	num=int(input())
	for i in range(1,num+1):
		bitwide+=len(str(i))
	print(bitwide)

	