'''
with open('f:\\test.txt','w') as f:
	f.write('Hello')
'''
with open('f:\\test.txt') as f:
	c=f.read(2)
	c2=f.read()
	print(c,c2)