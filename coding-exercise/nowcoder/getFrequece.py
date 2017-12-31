numset=list(input().split())
length=len(numset)
count=[]

for val in numset:
  flag=True
  for v in count:
    if val==v[0]:
      v[1]+=1
      flag=False
      break
  if flag:
	  count.append([val,1])
  
print(count)
for max in count:
  if max[1]>=length//2:
    print(max[0])
    break