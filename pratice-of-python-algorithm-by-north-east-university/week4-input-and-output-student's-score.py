'''
编写程序，输入10个学生的学号和计算机科目成绩，存放于列表中，
存放方式为[[学号1,成绩1],[学号2,成绩2],...]。输出此列表，输出格式如下：
学号    成绩
学号1    成绩1
学号2    成绩2
...
提示：可以用列表的append方法添加一个列表作为它的元素。
可以用L[1][1]访问列表L中第二个列表元素中的第二个数值。
'''
total=3
print("当前操作：%d名学生学号，成绩录入中..."%total)
print('')
marks=[]
cnt=0
while cnt<total:
	marks.append(list(input("输入第%d名学生学号、成绩,空格分隔\n"%(cnt+1)).split()))
	cnt+=1
print("\n---学生成绩输出如下---\n")

print("%s    %s"%("学号","姓名"))
for stu in marks:
	print("%s    %s"%(stu[0],stu[1])) 