'''
找出n个数里最小的k个
每个测试输入包含空格分割的n+1个整数，
最后一个整数为k值,n不超过100
输出n个整数里最小的k个数。升序输出
3 9 6 8 -10 7 -11 19 30 12 23 5
# print(str.join(numSet[::-1]))
'''

numSet=list(input().split())
# k=int(input())
k=int(numSet.pop())
# print('1-',numSet)

for index in range(len(numSet)):
	numSet[index]=int(numSet[index])
# print('before sorted-',numSet)
numSet.sort()
# print('after sorted-',numSet)
for i in range(k-1):
	print(numSet[i],' ',end='',sep='')
print(numSet[k-1])