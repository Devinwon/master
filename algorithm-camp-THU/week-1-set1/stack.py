
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
"""
# -*- coding: UTF-8 -*-
class StackUnderflow(ValueError):
	pass

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

	def is_empty(self):
		return self._element==[]

count=int(raw_input())
st=Stack()
for _ in range(count):
	cmdStr=raw_input():
	if cmdStr[0]=='1':
		st.push(cmdStr[2:])
	elif cmdStr[0]=='2':
		print st.pop()
	elif cmdStr[0]=='3':
		# 只是询问位置元素,并打印,
		loc=int(cmdStr[2:])
		sTemp=Stack()
		# 临时存储




