
exampleno=int(input())
exampleset=[]
for i in range(exampleno):
	exampleset.append(input())
'''
这个顺序很重要
'''
re_phonenumber=[[0,'EIGHT','G'],[2,'ZERO','Z'],[8,'SIX','X'],[9,'SEVEN','S'],[7,'FIVE','V'],[6,'FOUR','F'],[5,'THREE','R'],[4,'TWO','T'],[3,'ONE','O'],[1,'NINE','E']]

phonenum=[]

def Isinsample(substr,desstr):
	flag=True
	for s in substr:
		if s not in desstr:
			flag=False
			break
	return flag

def delsubstr(substr,desstr,cnt):
	for s in substr:
		desstr=desstr.replace(s,'',cnt)
	return desstr

for sample_index in range(len(exampleset)):
	phonenum=[]
	for val in re_phonenumber:
		if Isinsample(val[2],exampleset[sample_index]) :
			cnt=exampleset[sample_index].count(val[2])
			# phonenum.append(val[0])
			phonenum.extend([val[0]]*cnt)
			#需要将匹配从sample中的删掉
			# print('phonenum',phonenum)
			# 获取满足条件的个数
			exampleset[sample_index]=delsubstr(val[1],exampleset[sample_index],cnt)
			# 更新了需要重新开始扫描，否则漏掉了
			# print('after',exampleset[sample_index])
			# break
			if not exampleset[sample_index]:
				break
	phonenum.sort()
	print(''.join('%s'%val for val in phonenum))
	



