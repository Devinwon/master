import gc

class People():
	name=''
	blood=''
	gender=''
	__money=''

	def __str__(self):
		return "这里重写类People()内部方法，自动被调用了,\
		如果没有重写，看到的将是形如:<__main__.People object at 0x00000000021DAB70>"
	'''
	同理还是有
	构造函数：__init__
	析构函数：__del__
	显示调用析构函数
	del 对象名
	'''

# 这里提供了默认参数
	def __init__(self,name='Bob',blood='O',gender='male',money='$10'):
		print('正在初始化')
		self.name=name
		self.blood=blood
		self.gender=gender
		self.__money=money


	def __del__(self):
		print('正在释放内存')


if __name__=='__main__':
	Jenney=People('Jenney','AB','female','$9090')
	print(Jenney.name)
	Jordan=People(name='Jordan')
	print(Jordan.name)
	# Pytho垃圾回收，引用计数，为0表示已经全部释放饿
	print(gc.collect())
	del Jordan
	print('Jordan已经释放')
	print(Jenney.name)
	del Jenney
	print('Jenney已经释放')

