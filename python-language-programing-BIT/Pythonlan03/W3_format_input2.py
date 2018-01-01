'''
Created on 2017年4月12日

@author: Administrator
'''
nmset='Tom','Jack','Tinayye','Mickay'
for i in range(len(nmset)):
    #print("Names：{0:*<9}".format(nmset[i])+"blankorNot")
    #print("Names：{0:*>9}".format(nmset[i]))
    print("Names：{0:^9}".format(nmset[i]))
print("Names：{0:*>15.4f}".format(123456.789123))
print("对字符串进行切片："+"{0:.4}".format("ABCEFG123456"))#ABCE
