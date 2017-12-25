def prtgap(g):
    print(" "*g,end='')

def prtstar(c,prtchar):
    print(prtchar*c)

maxline=int(input("input max line number:"))
prtchar=input("input one char to print:")
center=(maxline+1)//2
cnt=0
for i in range(center-1,-1,-1):
    prtgap(i)
    prtstar(2*cnt+1,prtchar)
    cnt+=1

for i in range(1,center):
    prtgap(i)
    cnt-=1
    prtstar(2*cnt-1,prtchar)
