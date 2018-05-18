"""
猫可以：喵喵叫、吃、喝、拉、撒
狗可以：汪汪叫、吃、喝、拉、撒

要求：分别为猫和狗创建一个类，实现他们所有的功能
"""

class Animal():
	nm=""
	def __init__(self):
		nm=""

	def p(self):
		print(self.nm+"叫")

	def eat(self):
		print("吃")

	def drink(self):
		print("喝")

	def lala(self):
		print("拉")

	def sasa(self):
		print("撒")

class Cat(Animal):
	nm=""
	def __init__(self):
		self.nm="喵喵"

class Dog(Animal):
	nm=""
	def __init__(self):
		self.nm="汪汪"

c=Cat()
d=Dog()

c.p()
c.eat()
c.drink()
c.lala()
c.sasa()

d.p()
d.eat()
d.drink()
d.lala()
d.sasa()

		