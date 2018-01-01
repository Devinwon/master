'''
编写程序计算下图所示二叉树结点的最大值，
要求用嵌套列表的形式来定义该二叉树，
且需要自己定义函数实现最大值的计算

注意二叉树的分支遍历，如果类似这样编码
return getMaxnum(tree[1],imax)就只遍历了左子树
'''
# 由于二叉树是无序的，需要遍历比较查找最大值
tree=[
				30,

				[52,
					[23,[],[]],
					[74,[],[]],
				],

				[15,
					[86,[],[]],
					[10,[],[]]
				]

			]

def getMaxnum(tree,imax):
	if tree!=[]:
		if imax==None:
			imax=tree[0]

		elif imax<tree[0]:
			imax=tree[0]

		# 注意二叉树的分支遍历，如果类似这样编码
		# return getMaxnum(tree[1],imax)就只遍历了左子树
		# 这里分别记录左右子树最大值，然后三者比较
		lmax=getMaxnum(tree[1],imax)
		rmax=getMaxnum(tree[2],imax)
		
		if lmax>imax:
			imax=lmax
		if rmax>imax:
			imax=rmax
		
	return imax

print(getMaxnum(tree,None))
			

'''
# 使用了全局变量，不提倡
imax=""
def getMaxnum(tree):
	global imax
	if tree!=[]:
		if type(imax)==str:
			imax=tree[0]
		elif imax<tree[0]:
			imax=tree[0]
		getMaxnum(tree[1])
		getMaxnum(tree[2])
	return imax

print(getMaxnum(tree))
'''




'''
# 先序遍历树
def preOrder(tree):
	if tree!=[]:
		print(tree[0],'',end='')
		preOrder(tree[1])
		preOrder(tree[2])

preOrder(tree)
'''
