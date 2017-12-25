'''
编写程序，求一元二次方程ax^2+bx+c=0的解。
要求：输入a、b、c的值，如果a等于0，输出“a不能为0，不是一元二次方程”；
否则输出方程解的情况（无实数解、有一个实数解并输出该解、有两个实数解并输出）。

'''
from math import sqrt
try:
	a=eval(input("a="))
	if (not a):
		print("a不能为0")
	else:
		b=eval(input("b="))
		c=eval(input("c="))
	dt=b**2-4*a*c

	if dt<0:
		print("无实数解")
	elif dt ==0:
		x=-b/(2*a)
		print("有一个实数解,x=%f"%x)
	else:
		x1=(-b-sqrt(dt))/(2*a)
		x2=(-b+sqrt(dt))/(2*a)
		print("有2个实数解,x1=%f,x2=%f"%(x1,x2))

except:
	print("Input error")
	pass

