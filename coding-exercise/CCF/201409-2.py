"""
即肉体思路：
x坐标轴排序

然后两重循环，分别检查每个是否与其他的重叠，重叠需要删除

多个的问题变成两两问题

明天继续
"""



n=int(input().strip())
martrix=[]
for i in range(n):
	martrix.append(list(map(int,input().strip().split())))
