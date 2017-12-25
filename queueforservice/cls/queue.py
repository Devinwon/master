class Queue():
	items=[]
	def __int__(self):
		self.items=[]

	def isEmpty(self):
		return self.items==[]

	def enque(self,item):
		return self.items.insert(0,item)

	def deque(self):
		return self.items.pop()

	def size(self):
		return len(self.items)

	def preitem(self):
		if  self.size()==0:
			return  0
		else:
			return self.items[0]
			