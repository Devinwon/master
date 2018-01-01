'''
find and print  the max number in a binary disorder tree

这个需要事先知道树的最小值，否则结果出错，
如果树元素全部为负结果就不正确
个人认为并不具有通用性
'''

def getmax(root):
    if root==[]:
        return 0
    maxnum=root[0]
    lmax=getmax(root[1])
    rmax=getmax(root[2])
    
    if lmax>maxnum:
        maxnum=lmax
    if rmax>maxnum:
        maxnum=rmax
    
    return maxnum
tree=[30,
 [52,
 [23,[],[]],
 [74,[],[]]
 ],
 [15,
 [86,[],[]],
 [10,[],[]] ]
 ]
maxn=getmax(tree)
print(maxn)