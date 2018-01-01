'''
读入一个字符串，内容为英文，输入其中出现最多的单词，要求：

(1) 仅考虑单词，不计算标点符号；

(2) 同一个单词的大小写形式合并计数，统一以小写输出；

(3) 如果两个单词出现的次数相同，输出字母序最小的单词
'''
# this is a python code by Python
s=input()
s=s.lower()
lst=s.split()
lst.sort()
cnt=0
maxstr=""
for v in lst:
	if v.isalpha() and lst.count(v)>cnt:
		cnt=lst.count(v)
		maxstr=v
print(maxstr)


