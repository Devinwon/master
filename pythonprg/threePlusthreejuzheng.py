#threePlusthreejuzheng.py
import math
sum=0.0
lst=[1,2,3,4,5,6,7,8,9]
# row=int(sqrt((len(lst))))
row=3
for r in range(row):
    sum+=lst[r*row+r]
print(sum)
