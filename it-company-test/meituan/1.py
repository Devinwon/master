# raw_input()
cnt=int(input())
num=map(int,input().split())
num=list(num)
rel=0

def dividBysevern(d):
	return  d%7==0

for  outi in range(cnt-1):
	for inneri in  range(outi+1,cnt):
		c=int(str(num[outi])+str(num[inneri]))
		if dividBysevern(c):
			print(c)
			rel+=1
		c=int(str(num[inneri])+str(num[outi]))
		if dividBysevern(c):
			print(c)
			rel+=1
print (rel)
