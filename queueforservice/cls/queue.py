
'''
queue
----------
|||.......
----------
import random,time
'''

class Queue():
	items=[]
	def __int__(self):
		self.items=[]

	def isEmpty(self):
		return self.items==[]

	# insert(index,item),index索引对应位置前插入元素
	# return self.items.insert(-1,item)
	def enque(self,item):
		self.items.append(item)

	# 队首元素出列
	def deque(self):
		del self.items[0]

	def size(self):
		return len(self.items)

	def fstitem(self):
		return self.items[0]

	def prt(self):
		print(self.items)

'''
q=Queue()
def test_empty():
	print(q.isEmpty())

def test_enque(item=random.randint(1,1000)):
	q.enque(item)

def test_deque():
	q.deque()

def  test_fstitem():
	print(q.fstitem())

if __name__=="__main__":
	test_empty()
	for _ in range(5):
		time.sleep(0.3)
		test_enque(item=random.randint(1,1000))
	test_empty()
	print(q.prt())
	# get head item and remove
	print(q.fstitem())
	q.deque()
	print(q.prt())
'''
