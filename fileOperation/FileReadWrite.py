def readPerline():
	file=open("filename.txt",'r')
	while True:
		content=file.readline() # read per line
		print(content)
		content=content.strip().split()
		name=content[0]
		# if content=="":
		print(name)
		break

def readLines():
	file=open("filename.txt",'r')
	content=file.readlines() # read lines once
	print(content)
	'''
	while True:
		content=content.strip().split()
		name=content[0]
		# if content=="":
		print(name)
		break
	'''
# readPerline()
# readLines()
f="filename.txt"
f.open('r')
rel=f.readlines()
f.close()
print(rel)
