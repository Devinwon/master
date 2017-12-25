n=(input())
if '.' in n :
	n=float(n)
else:
	n=int(n)

cnt=0
for i in range(0,6):
	if cnt!=5:
		print(n**i," ",end='')
		cnt+=1
	else:
		print(n**i)
