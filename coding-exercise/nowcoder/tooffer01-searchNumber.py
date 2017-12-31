class solution:
	def Find(self,target,array):
		flag=False
		for outer in array:
			if target in outer:
				flag=True
				break
		return flag

