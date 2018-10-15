class Dequeue():
	def __init__(self):
		self.items=[]

	def isEmpty(self):
		return self.items==[]
	
	def enqueue(self,var):
		self.items.insert(0,var)
	
	def dequeue(self):
		return self.items.pop()

	def size(self):
		return len(self.items)

dq=Dequeue()
nmlst=["Bill","David","Susan","Jane","Kent","Brad"]

circle=7
for v in nmlst:
	dq.enqueue(v)

while dq.size()>1:
	for cnt in range(2,circle+1):
		dq.enqueue(dq.dequeue())
	print(dq.dequeue())
print('---')
print(dq.dequeue())



