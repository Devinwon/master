class People():
	name='bob'
	blood='o'
	gender='male'
	# __money私有成员，外部不能直接访问
	__money='$9999'

	# 定义成员函数，公有
	def bloodinfo(self):
		print('%s blood type is %s'%(self.name,self.blood))

	def qry(self):
		print('Default amount of money is %s'%self.__money)

	def setMoney(self,newmoney):
		# 注意这里self不能掉，否则无效
		self.__money=newmoney

	# 演示无实例化情况下调用成员函数
	def noinstancetocall(self):
		print('called by no instance')

	noINS=classmethod(noinstancetocall)

		# 注意没有self
	def staticmethodcall():
		print('called by static method')

	stamethod=staticmethod(staticmethodcall)

	'''
	当然如果觉得上面还要命名转换，比较麻烦的话，可以使用装饰器
	'''
	@classmethod
	def noinstancetocall2(self):
		print('called by no instance2')

	@staticmethod
	def staticmethodcall2():
		print('called by static method2')

if __name__=='__main__':
	Jenney=People()
	# 重写成员变量
	Jenney.name='Jenney'
	# 直接调用公有成员变量
	print(Jenney.blood)
	print(Jenney.name)
	Jenney.bloodinfo()

	# print(Jenney.__money) will wrong,call like below
	# 通过内部成员函数调用私有成员
	Jenney.qry()

	# 对私有成员的设置，公有直接设置，私有同样需要调用内部函数
	Jenney.setMoney('$9898')
	print('after set new money')
	Jenney.qry()

	''' 被classmethod处理过的函数，能被类直接调用，
	也能被对象调用（是继承的关系）
	该形式调用的话，其他成员变量、方法没有被加载到内存，
	仅仅只是该方法被加载
	'''
	People.noINS()
	Jenney.noINS()
	# 使用装饰器
	People.noinstancetocall2()
	Jenney.noinstancetocall2()

	'''
	staticmethod相当于全局函数，可以被类直接调用，
	可以被所有实例化对象共享，
	通过staticmethod()定义的静态方法没有self参数
	静态的话，预先将成员函数等全部加载进来供后续调用，占用内存较多，速度快
	动态的话，随着调用而加载，占用内存较小，速度稍微慢些
	'''
	People.stamethod()
	Jenney.stamethod()
	People.staticmethodcall2()
	Jenney.staticmethodcall2()

