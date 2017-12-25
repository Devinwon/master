#如何去掉print()默认的空格拼接，换行输出
#print()输出后默认换行（以end=""表示不换行），默认后面加空格(以sep=""表示无空格拼接)

s="Hello world"
print("打印字串s=",s,sep="")                 	#or s[0:]  
print("s的长度是len(s)=",len(s),sep="")          #print the length of s 
print("s的第一个字符s[0]=",s[0])
print("s的最后一个字符s[-1]=",s[-1])     	#print last char of s
print("\n----进行切片操作：----")
print("打印前三个字符s[0:3]:",s[0:3])        
print("打印末尾三个字符s[-3:]:",s[-3:]) 	#注意不能写成s[-3:0]或s[-3:-1],都是错误的

print("\n---删除字符两端的空格---")
start='123'
s2="  abc  "
sed="end"
print("start=",start,sep='')
print("   s2=",s2,sep='')
print("  sed=",sed,sep='')
print("join s2 Before:",start,s2,sed,sep="")
#s2.strip()并没有对s2本身做任何的更改，新的更改存储到了新的变量中，注意
'''
s2="  skfjk  "
s2.strip()
print(s2)后仍为"  skfjk  "，除非
print(s2.strip()),结果才为"skfjk",
'''
print("join s2 After :",start,s2.strip(),sed,sep='')