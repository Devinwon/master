isok=False
n=int(input().strip())
mylst=list(map(int,input().strip().split()))

outNum=sum(mylst)
if outNum>=0:
	isok=True

if isok:
	print("Wo jue de OK")
else:
	print("Wo jue de bu tai xing")
