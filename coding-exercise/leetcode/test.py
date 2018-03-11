'''
class Person:
	def __init__(self):
		pass
	def getAge(self):
		print __name__


p = Person()
p.getAge()

'''

'''
def bar(multiple):
	def foo(n):
		return multiple**n
	return foo
print(bar(2)(3))
'''


def dec(f):
	n = 3
	def wrapper(*args,**kw):
		return f(*args,**kw) * n
	return wrapper

@dec
def foo(n):
return n * 2


foo(2)=2(n)*2*3(n)=12
foo(3)=3(n)*2*3(n)=18