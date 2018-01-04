from time import strftime

# filenamed by date
filenm=strftime("%Y%m%d")
'''
with open(filenm+".txt","a+") as f:
	f.write("123\n")
'''

'''
文件不存在就自动创建
文件存在就删除内容，然后重新创建空的新文件
'''
outf=open("20180103.txt",'w')
outf.writelines(["Hello",' ',"World"])
outf.close()
inf=open('20180103.txt','r')
print(inf.read())

'''
遍历文件代码框架
# readlines()缺点，一次性读入文件过大会占据很多内存
file=open(somefile,'r')
for  line in file.readlines():
	# 处理一行文件内容
file.close()

# 简化代码框架
file=open(somefile,'r')
for  line in file:
	# 处理一行文件内容
file.close()
'''
