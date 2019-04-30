'''
队列实现排队叫号系统
实现功能：
--客户取号
--办理叫号
--查看排队
--我的进度
--退出系统
--write to file

'''

from cls.queue import Queue
from time import strftime
import os,time

queObj=Queue()
sn=0

def dispalyMenu():
	print("============Select Your Service============")
	print("1--客户取号")
	print("2--我的进度")
	print('          ')
	print("4--办理叫号")
	print("5--查看排队")
	print("6--退出系统")
	print("===========================================")


def officerCheck(pwd):
	if pwd=='admin':
		return True
	else:
		return False

def waiting(item):
	'''
	客户取号，并加入排队当中
	'''
	queObj.enque(item)


def scaning():
	'''
	业务人员查看全部排队，返回总的人数
	'''
	return queObj.size()


def doing():
	'''
	办理业务,队首人员出队
	'''
	time.sleep(1)
	queObj.deque()

def genID():
	'''
	用户排队编号生成,日期加流水号
	'''
	global sn
	dt=strftime("%Y%m%d")
	sn+=1
	return dt+"{:0>3d}".format(sn)

def personAhead(currentID):
	if queObj.size()>1:
		header=queObj.fstitem()
		sn=int(header[8:])
		myid=int(currentID[8:])
		return myid-sn
	else:
		return 0


if __name__=='__main__':
	while True:
		menuID=['1','2','4','5','6']
		dispalyMenu()
		choice=input("请选择：").strip()
		if choice in menuID:

			if choice==menuID[0]:
				# 取号，加入排队
				myid=genID()
				print("{}是你的服务号码，请牢记".format(myid))
				waiting(item=myid)

			elif choice==menuID[1]:
				currentID=input("请输入你的服务号:")
				print("你的前面还有：{} 人".format(personAhead(currentID)))

			else:
				pwd=input("身份验证:")
				if officerCheck(pwd):
					if  choice==menuID[2]:
						# 办理
						doing()

					elif choice==menuID[3]:
						# scaning
						print("当前排队人数：{}".format(scaning()))

					elif choice==menuID[-1]:
						print('\n退出系统')
						break
				else:
					print("身份验证失败")

		else:
			print("(x)选择错误,重新选择")






