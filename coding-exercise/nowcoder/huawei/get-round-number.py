'''
#description:#
写出一个程序，接受一个正浮点数值，输出该数值的近似整数值。
如果小数点后数值大于等于5,向上取整；小于5，则向下取整。

###Input description###
输入一个正浮点数值

###Output description###
输出该数值的近似整数值

#example#

###Input###
5.5

###Output###
6
'''

print(int(eval(input())+0.5))