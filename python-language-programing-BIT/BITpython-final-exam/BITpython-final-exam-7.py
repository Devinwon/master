'''
重复元素判定 ,输入的是一个列表，
判断其中是否有重复元素
注意eval()的用法，考试的时候这里用错了
'''

lst=eval(input())
ltoset=set(lst)
print(len(lst)==len(ltoset))

'''
lst.sort()
flag=True
for i in range(len(lst)-1):
	if lst[i]==lst[i+1]:
		flag=False
		break
print(flag)
'''
