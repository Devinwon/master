import random
rel=[]
cnt=0
while True:
	try:

		r=random.randrange(1,10)
		rel.append(r)
		cnt+=1
		if cnt>3:
			break
	except:
		pass

print(rel)

