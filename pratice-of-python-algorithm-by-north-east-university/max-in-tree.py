'''
编写程序计算下图所示二叉树结点的最大值，
要求用嵌套列表的形式来定义该二叉树，
且需要自己定义函数实现最大值的计算
'''
# 由于二叉树是无序的，需要遍历比较查找最大值
tree=[
				2,

				[52,
					[23,[],[]],
					[74,[],[]],
				],

				[15,
					[86,[],[]],
					[10,[],[]]
				]

			]

'''
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


# import time

def getMaxnum(tree,imax):
	if tree!=[]:
		if type(imax)==str:
			imax=tree[0]
			print(tree[0],'-')
		elif imax<tree[0]:
			print(tree[0],'-')
			print('before',imax)
			imax=tree[0]
			print('switch',imax)
		else:
			print(tree[0],'-')
			print('noswitch',imax)
		getMaxnum(tree[1],imax)
		# time.sleep(10)
		getMaxnum(tree[2],imax)
	return imax

print(getMaxnum(tree,""))


'''
# 先序遍历树
def preOrder(tree):
	if tree!=[]:
		print(tree[0],'',end='')
		preOrder(tree[1])
		preOrder(tree[2])

preOrder(tree)
'''
