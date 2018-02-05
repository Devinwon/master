name="Devin"
age=12
print("{0} is {1} years old".format(name,age))

print("{name} is my {relationship}".format(relationship="friend",name="Lily"))

lst=["Math",98]
lst2=["lvl1","lvl2"]
print("my {0[0]} is {0[1]}:{1[1]}".format(lst,lst2))

print("1234567890")
#默认空格填充,居中对齐
print("{:^10}".format("Hello"))

#指定#填充
print("{:#^10}".format("Hello"))

#右对齐
print("{:<10}".format("Hello"))

#左对齐
print("{:>10}".format("Hello"))

print("{:.4f}".format(1234.567))

print("{:b}".format(10))
print("{:d}".format(10))
print("{:o}".format(10))
print("{:x}".format(10))

print("{:,}".format(123456))