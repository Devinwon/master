'''
两个列表元素之间最小的差（绝对值）
A=[3,4,5,6]
B=[12,5,0,9]
最小的差为
'''

A=[-9,4,5,6]
B=[12,51,7,9]

c=[]
for i in A:
	c.append((i,'A'))
for j in B:
	c.append((j,'B'))
c.sort()
print(c)

temp=abs(c[0][0]-c[1][0])

for L in range(1,len(c)-2):
	if abs(c[L][0]-c[L+1][0])<temp:
		temp=abs(c[L][0]-c[L+1][0])

print(temp)