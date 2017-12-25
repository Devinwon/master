'''
hello xiao mi
mi xiao hello
原始方法
'''

# while True:
# 	str=input()
# 	if len(str)!=0:
# 	  lst=str.split()
# 	  while lst:
# 	    if len(lst)==1:
# 	    	print(lst.pop())
# 	    else:print(lst.pop(),' ',end='',sep='')
# 	else:break

'''
精简方法
'''
words = input().split()
print(' '.join(words[::-1]))
# 从后向前用空格将元素连接起来
# 注意切片的这个用法，最简单，
# lst[::-1],从后向前遍历
# lst[::2],从前往后索引0,2,4..遍历
#  newstr=list(reversed(str)) 反转列表

