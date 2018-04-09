n=input()
rel=[]
for e in n:
	rel.append(e)
rel.sort()

print(''.join(rel[::-1]))
