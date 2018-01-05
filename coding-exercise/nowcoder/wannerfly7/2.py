
'''
题目描述 
codeJan 非常喜欢旅行。现在有 n 个城市排在一条线上，并且 codeJan 的位置不和任何一个城市的位置重叠。
codeJan 想要游览 m 个城市，同时因为时间是不断变化的，游览一个城市多次也是允许的，但是不能永远待在一个城市，否则那样太无聊了。给出这些城市的位置，codeJan 想要知道游览 m 个城市至少需要走多少米？
输入描述:
第一行是一个T≤20代表测试组数。
每组第一行是三个正整数n,m,p，分别代表城市数量、codeJan想要浏览的城市数量和codeJan当前的位置(单位为米)。
第二行包含n个正整数pos[i]表示第i个城市的位置，单位为米。
输入保证pos[i]<pos[i+1](i∈[1,n−1])，并且p ̸=pos[i](i∈[1,n])。
输出描述:
对于每组输入数据输出一个正整数表示 codeJan 至少需要走的距离。

输入

3 
2 2 2 
1 3 
2 2 1 
2 3 
4 3 4 
1 3 5 6
输出

3
2
3
说明

对于第一个样例的坐标最优移动顺序可以是：2→3→1，移动距离一共是3。
对于第二个样例的坐标最优移动顺序可以是：1→2→3，移动距离一共是2。
对于第三个样例的坐标最优移动顺序可以是：4→5→6→5，移动距离一共是3。
'''


groupnum=int(input())
rel=[]
cnt=0
while cnt<groupnum :
	cnt+=1

	n_citynum,m_leastvisit_citynum,p_pos=input().split()
	n_citynum=int(n_citynum)
	m_leastvisit_citynum=int(m_leastvisit_citynum)
	p_pos=int(p_pos)

	# 城市的位置坐标顺序递增
	loc=input().split()
	for i in range(len(loc)):
		loc[i]=int(loc[i])

	# 移动的距离
	visitednum=0
	step=0
	while visitednum<m_leastvisit_citynum:
		if p_pos<loc[0]:
			visitednum+=1
			step+=abs(p_pos-loc[0])
			visitednum+=1

	loc.append(p_pos)
	p_pos_index=loc.index(p_pos)



def least_move(poc,loc,visitnum):
	step=0
	visited=0
	if poc<loc[0]:
		if visitnum==1:
			step+=abs(loc[0]-poc)
			visited+=1
		elif visitnum>1:

		



