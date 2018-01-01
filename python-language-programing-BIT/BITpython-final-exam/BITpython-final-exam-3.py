'''
写一个程序进行货币间币值转换，其中：

人民币和美元间汇率固定为：1美元 = 6.78人民币。

程序可以接受人民币或美元输入，转换为美元或人民币输出。
人民币采用￥符号或RMB表示，美元采用$或USD表示，符号和数值之间没有空格。
'''
money=input()
if money[0]=='$':
	money='{0:.2f}'.format(eval(money[1:])*6.78)
	print('￥',money,sep='')
elif money[0]=='R':
	money='{0:.2f}'.format(eval(money[3:])/6.78)
	print('USD',money,sep='')
elif money[0]=='￥':
	money='{0:.2f}'.format(eval(money[1:])/6.78)
	print('$',money,sep='')
else:
	money='{0:.2f}'.format(eval(money[3:])*6.78)
	print("RMB",money,sep='')