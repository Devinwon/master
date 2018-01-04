from time import strftime

# filenamed by date
filenm=strftime("%Y%m%d")
'''
with open(filenm+".txt","a+") as f:
	f.write("123\n")
'''

'''
with open(filenm+".txt","r") as f:
	for c in f:
		print(c)
'''

'''
# 整个文件输出
str_nm=input("输入文件的名称")
f =open(str_nm,'r')
data=f.read()
print(data)
'''

'''
# 读取前面5行,注意readline()以换行符结束
# rendlines()返回整个文件内容的列表，每项以换行符为结尾的字符串
f =open("20180104.txt",'r')
for i in range(5):
	line=f.readline()
	# 注意这里把每一个空行删除了
	print(line[:-1])
'''