class Life():
	life=0
	name='X'
class People():
	name='human'
	life=70
	def say(self):
		print('can say')

class Chinese(People):
	name='Chinese'
	life=99
	def say(self):
		print('say chinese')

class American(People):
	name='American'
	life=90
	def say(self):
		print('say English')		

class England(People,Life):
	name='eeeeeeee'

class England2(Life,People):
	pass

'''
对于多继承，如果多个父类的同一属性值不同，
子类按继承先后顺序取值，以找到的首个父类，满足的属性值为准
初始化也一样
'''
if __name__=='__main__':
	person=People()
	print(person.name)
	person.say()

	Misslee=Chinese()
	print(Misslee.name)
	Misslee.say()

	Jenney=American()
	print(Jenney.name)
	Jenney.say()

	xman=England()
	print(xman.name)

	xwoman=England2()
	print(xwoman.name)

