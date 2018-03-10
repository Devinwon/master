'''
#description:#
写出一个程序，接受一个十六进制的数值字符串，
输出该数值的十进制字符串。（多组同时输入 ）

###Input description###
输入一个十六进制的数值字符串。

###Output description###
输出该数值的十进制字符串。

#example#

###Input###
0xA

###Output###
10
'''
while True:
	try:
		print(int(input(),16))
	except:
		break