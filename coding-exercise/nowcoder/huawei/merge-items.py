'''
#description:#
数据表记录包含表索引和数值，请对表索引相同的记录进行合并，
即将相同索引的数值进行求和运算，输出按照key值升序进行输出。

###Input description###
先输入键值对的个数
然后输入成对的index和value值，以空格隔开

###Output description###
输出合并后的键值对（多行）

#example#

###Input###
4
0 1
0 2
1 2
3 4

###Output###
0 3
1 2
3 4
'''
while  True:
	try:
		cnt=int(input())
		rel_dict={}
		while cnt:
			k,v=input().split()
			k,v=int(k),int(v)
			if rel_dict.get(k) is None:
				rel_dict[k]=v
			else:
				rel_dict[k]+=v
			cnt-=1

		# print(sorted(rel_dict))
		# print(sorted(rel_dict.keys()))
		# print(sorted(rel_dict.items()))
		index_lst=sorted(rel_dict.keys())
		for i in index_lst:
			print(i,rel_dict[i])
	except:
		break


'''
from collections import defaultdict
while True:
    try:
 
        a,dd=int(input()),defaultdict(int)
        for i in range(a):
            key,val=map(int,input().split())
            dd[key]+=val
        for i in sorted(dd.keys()):
            print(str(i)+" "+str(dd[i]))
 
    except:
        break
'''
# 多使用迭代，map的用法