'''
寻找一个数的完美平方数（如，1，4，9等），
从小到大输出
要求完美平方数的和等于这个数
并且完美平方数尽可能少
10=9+1（OK）
10=4+4+1+1
'''
import math
num=int(input())
rel=[]
while(num>0):
	temp=int(math.sqrt(num))
	rel.append(temp**2)
	num=num-temp**2
print(rel)