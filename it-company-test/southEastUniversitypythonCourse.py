'''
东南大学-python课程

寻找第n个默尼森数。
代码格式如下：
def prime(num):
    ...
def monisen(no):
    … …
    return  xxx

print(monisen(int(input())))    #此处不需要自己输入，只要写这样一条语句即可，主要完成monisen()函数（4分）

经典程序设计问题：找第n个默尼森数。P是素数且M也是素数，并且满足等式M=2**P-1，则称M为默尼森数。
例如，P=5，M=2**P-1=31，5和31都是素数，因此31是默尼森数。
输入格式:按提示用input()函数输入
输出格式：int类型
输入样例：4
输出样例：127
'''

'''
一个数除了1跟本身外，不能被任何数整除的数字就是素数
'''
def prime(num):
	flag=True
	for i in range(2,num//2+1):
		if num%i==0:
			flag=False
			break
	return flag

'''
返回默尼森数，M=2**P-1，二者都是素数，且满足前述条件
'''
def monisen(num):
	index=0
	p=2
	while index<num:
		if prime(p) and prime(2**p-1):
			index+=1
		p+=1
	return 2**(p-1)-1
print(monisen(int(input())))


