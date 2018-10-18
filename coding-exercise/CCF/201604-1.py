"""
所有评测用例满足：1 ≤ n ≤ 1000，

每天的销售量是不超过10000的非负整数。

求不满足连续性的点个数
"""

n=int(input().strip())
nsales=list(map(int,input().strip().split()))
cnt=0

for inx in range(n-2):
	if not(nsales[inx]< nsales[inx+1]< nsales[inx+2] or nsales[inx]> nsales[inx+1]> nsales[inx+2]):
		cnt+=1
print(cnt)



