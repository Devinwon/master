class LinkNode():
	"""docstring for LinkNode
	default parameter located in __init__(),not essential 
	linkList store students' score
	

	def __init__(self,score=0,name=None):
		self.score = score
		self.name = name
	"""
	def __init__(self):
		self.score = 0
		self.name = ""
		self.next=None
# 建立链表头部
head=LinkNode()

# 当前没有下一个元素
head.next=None

# 设置存取指针的位置
ptr=head
lik=LinkNode()

		