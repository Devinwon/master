# -*- coding: UTF-8 -*-
"""
描述
实现一个栈，完成以下功能：

入栈
出栈
询问栈中位置Y是谁

一开始栈为空。栈中的位置从1开始（即栈底位置为1）。

输入
第一行一个整数n，表示操作个数。

接下来n行，每行第一个数字表示操作（见描述）：

若为数字1，则接下来有一串字符串X，表示将X压入栈中。
若为数字2，表示弹出栈顶（保证栈非空），并输出出栈的这个人。
若为数字3，则接下来有一个整数Y，表示询问栈中位置Y是谁（保证位置Y合法），并输出名字。
输出
将所有操作2和操作3输出，一行一个。

视图将查找索引存储起来,一次性检索,提高效率

检索顺序:1 3 2 3 4
检索排序:[1,2,3,3,4]
记录他们出现的值
{1:value,2:value,3:value,4:value}


"""

# define exception
class StackUnderflow(ValueError):
	pass

# define stack()
class Stack():
	_element=[]
	def __init__(self, ):
	  self._element=[]

	def push(self,v):
		self._element.append(v)

	def pop(self):
		if self._element==[]:
			raise StackUnderflow("in pop()")
		return self._element.pop()

	def top(self):
		if self._element==[]:
			raise StackUnderflow("in top()")
		return self._element[-1]

	def empty(self):
		return self._element==[]

def getValueByIndex(st,locLst,length):
	lsTemp=[]

	# 栈中剩下不弹出的元素数量
	leftInst=min(locLst)-1
	for _ in xrange(length-leftInst):
		lsTemp.append(st.pop())
	for l in locLst:
		print lsTemp[leftInst-l]

	while lsTemp:
		st.push(lsTemp.pop())


count=int(raw_input())
st=Stack()
length=0
locLst=[]
for _ in xrange(count):
	cmdStr=raw_input()
	# in stack
	if cmdStr[0]=='1':
		st.push(cmdStr[2:])
		length+=1

	# out stack
	elif cmdStr[0]=='2':
		if locLst==[]:
			print st.pop()
			length-=1
		else:
			getValueByIndex(st,locLst,length)
			locLst=[]
			print st.pop()
			length-=1


	# print value in loc		
	elif cmdStr[0]=='3':
		loc=int(cmdStr[2:])
		locLst.append(loc)

if locLst:
	getValueByIndex(st,locLst,length)
	locLst=[]


