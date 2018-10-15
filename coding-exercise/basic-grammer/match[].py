class Stack():
	def __init__(self):
		self.items=[]

	def isEmpty(self):
		return self.items==[]

	def push(self,par):
		self.items.append(par)

	def pop(self):
		self.items.pop()

	def size(self):
		return len(self.items)

exp='(5+6)*(7+8)/(4+3)'
s=Stack()
flag=True
for v in exp:
	if v=='(':
		s.push(v)
	elif v==')':
		if not s.isEmpty:
			s.pop()
		else:
			flag=False
			break

if s.isEmpty() and flag:
	print("OK") 
else:
	print("No")


