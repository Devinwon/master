"""
列表嵌套 多重字段 排序
"""

# lst=[('01',20),('02',100),('08',90),('03',80),('03',93),('05',80)]

"""
第一种情况
列表中嵌套列表或者元组,
对第一个(子)元素进行排序
"""
"""
lst.sort()
print(lst)
# 或者,
print(sorted(lst))
"""

"""
第二种情况
列表中嵌套列表或者元组,
对非第一个(子)元素进行排序
"""
"""
print(sorted(lst,key=lambda x:(x[1])))

# 或者,py3.6中 sort()\ sorted()均没有cmp参数,只有key
def mkcmp(x):
	return x[1]
print(sorted(lst,key=mkcmp))

# 或者
from operator import itemgetter
print(sorted(lst,key=itemgetter(1)))

"""



"""
第三种情况
列表中嵌套列表或者元组,
对元素多字段进行排序
实现对多重进行不同的升降排序,1-升,2-降
print(sorted(lst,key=lambda x:(x[1],-int(x[0]))))
"""

"""
from operator import itemgetter
print(sorted(lst,key=itemgetter(0,1)))
print(sorted(lst,key=itemgetter(1,0)))
"""

"""
第四种情况
列表中字典,
按指定键排序
"""
"""
"""
lst=[{"name":"Joe","age":23,"grade":90},
		{"name":"Devin","age":20,"grade":80},
		{"name":"Kevin","age":19,"grade":93},
		{"name":"Robot","age":18,"grade":80},
		{"name":"Amy","age":24,"grade":70},
		{"name":"Ham","age":22,"grade":88},
		{"name":"Bob","age":23,"grade":82},
		{"name":"Aob","age":25,"grade":82}
		]


"""
"""
relsort=sorted(lst,key=lambda x :(-(x["grade"]),x['name']))
for v in relsort:
	print("{:8}".format(v["name"]),v["grade"])

"""
lst=[(1,2,3),(3,4),(0)]
print(sorted(lst,key=lambda x :len(str(x))))
"""