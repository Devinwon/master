
'''
从中解析触最小的电话号码
'''
'''
OHWETENRTEO
3-->HWTERTEO
4-->HERTE
5--''
'''
# 解析数目
exampleno=int(input())
# 待解析的字符串OHWETENRTEO
exampleset=[]
for i in range(exampleno):
	exampleset.append(input())


# 解析规则
re_phonenumber=[[0,'EIGHT'],[1,'NINE'],[2,'ZERO'],[3,'ONE'],[4,'TWO'],[5,'THREE'],[6,'FOUR'],[7,'FIVE'],[8,'SIX'],[9,'SEVEN']]

# 存储解析出来的号码,排序后顺序输出就是最小的
phonenum=[]
'''
规则中字串substr是否在输入样例deslst字串形式当中
'''
def Isinsample(substr,desstr):
	flag=True
	for s in substr:
		if s not in desstr:
			flag=False
			break
	return flag

def delsubstr(substr,desstr):
# 确定了字串在目的当中
	for s in substr:
		desstr=desstr.replace(s,'',1)
		# 一次替换了多个导致结果异常
		# print('in function',desstr)
	return desstr

def prt(phonenum):
	for val in phonenum:
		print(val,end='')
	print()

for sample_index in range(len(exampleset)):
	phonenum=[]
	while exampleset[sample_index]:
		for val in re_phonenumber:
			# print('before,example',exampleset[sample_index],'val',val[1])
			if Isinsample(val[1],exampleset[sample_index]) :
				phonenum.append(val[0])
				#需要将匹配从sample中的删掉
				# print('phonenum',phonenum)
				exampleset[sample_index]=delsubstr(val[1],exampleset[sample_index])
				# 更新了需要重新开始扫描，否则漏掉了
				# print('after',exampleset[sample_index])
				# break
	phonenum.sort()
	prt(phonenum)
	



