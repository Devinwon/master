"""
3
CS301111 15:30:28 17:00:10
SC3021234 08:00:00 11:25:25
CS301133 21:45:00 21:58:40
"""
total=int(input().strip())
records=[]
for i in range(total):
	records.append(input().strip().split())
# find out the earliest and latest
# sort 
rel=sorted(records,key=lambda x:x[1])
print(rel[0][0],'',end='')
rel=sorted(records,key=lambda x:(x[2]))
print(rel[-1][0])
