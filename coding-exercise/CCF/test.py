lst=[1,2,34]

t=lst[0]
lst=lst[1:]

# lst只是一个标签而已，所指向的地址已经发生变化，所以t的值不会是2
print(t)

print(lst)

