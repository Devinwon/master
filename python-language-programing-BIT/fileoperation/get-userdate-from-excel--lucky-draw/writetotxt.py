'''
将一个列表的数据存储到文件当中
'''

def writeTotxt(src_list):
	with open("userdata.txt",'w+') as f:
		f.write("中奖者名单 \n")
		for v in src_list:
			f.write(v+'\n')
	f.close()
