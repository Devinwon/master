pnow=int(input())
pmark=[]
for v in list((input().split())):
	pmark.append(int(v))
pmark.sort()
print(pmark)

# 最少出题的数量
pset=0
if len(pmark)==1:
	pmark.pop()
	pset+=2
else:
	while(len(pmark)>=2):
		if pmark[1]-pmark[0]>20:
			pset+=2
			pmark=pmark[1:]
		elif (pmark[1]-pmark[0])>10 and (pmark[1]-pmark[0])<=20 :
			pset+=1
			pmark=pmark[2:]
		else:
			# pmark.pop(pmark[0])
			pmark=pmark[1:]
			mid=pmark[0]
			pmark=pmark[1:]
			if len(pmark)>=1:
				if pmark[0]-mid<=10:
					pmark=pmark[1:]
				else:
					pset+=1
			else:
				pset+=1
				# 循环终止

print(pset+len(pmark)*2)





'''
30  60   1000
相邻2各数大于20 不能在一个组
需要2题与其相匹配

往下循环，
相邻两数10< <20可以匹配，
1

后面题目跳2
《10，看后面的数
'''



