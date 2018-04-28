"""
规定k[n]表示k个n
如2[w]表示2个ww,k在1-9之间

写程序进行解析
注意可能会嵌套

2[3[ab]]表示ababab*2->abababababab

使用递归

返回的值的时候
折腾了弄了半天,把值返回就可以,

不要尝试在函数内部进行输出,很容出错

"""
def decode(s):
	num=int(s[0])
	while True:
		s=s[2:-1]
		if '[' in s:
			return num*decode(s)
		else:
			return num*s
print(decode('2[1[2[ko]]]'))

