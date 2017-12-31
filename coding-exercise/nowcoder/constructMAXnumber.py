# numberset=[]
# while((input())):
# 	numberset.append(list(input().split()))
# # print(numberset)

# for val in numberset:
# 	val.sort()
# 	print(''.join(val[::-1]))


'''
2
75 755
'''
numberset=[]
while True:
	temp=input()
	if temp :
		numberset.append(list(input().split()))
	else:break

# print(numberset)

for val in numberset:
	val.sort()
	print(''.join(val[::-1]))
