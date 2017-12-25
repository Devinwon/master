
'''
定义函数countchar()
按字母表顺序统计字符串中所有出现的字母的个数
（允许输入大写字符，并且计数时不区分大小写）。
def countchar(str):
      ... ...
     return a list
if __name__ == "__main__":
     str = input()
     ... ...
     print(countchar(str))

输入格式:
字符串

输出格式：
列表

输入样例：
Hello, World!

输出样例：
[0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 3, 0, 0, 2, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0]     
'''

# 数据结构构造
# A-Z
charList=list(range(65,91))
# print(charList)
for i in range(len(charList)):
	charList[i]=chr(charList[i]) 
# print((charList))


def countchar(s):
	# 首先判断是否字母
	count=[0]*26
	for i in range(len(s)):
		# 注意这里的s[i].upper(),s[i]并没有被更改
		if s[i].isalpha() and s[i].upper() in charList:
			count[charList.index(s[i].upper())]+=1	
	# print(len(count))
	return count

if __name__ == "__main__":
  s = input()
  print(countchar(s))