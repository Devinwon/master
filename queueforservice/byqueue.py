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
import os

singleTake=5
queueforMeal=Queue()
cmd='start'


'''
当前最后的排队编号
'''
def getPresentNO():
	return int(queueforMeal.fstitem())


'''
获取票号
''' 
def getNO():
	myNO=getPresentNO()+1
	queueforMeal.enque(myNO)
	guestInfo(myNO)


'''
打印小票
Your No is :
%d persons ahead of you
It will take you %d minutes to wait
'''
def guestInfo(guestNO):
	print('---------------------------------------')
	print('你的排队号码:%d'%guestNO)
	print("你的前面有:%d人"%(queueforMeal.size()-1))
	timetoWait=(queueforMeal.size()-1)*singleTake
	if timetoWait<60:
		print("大约还需要等待:%d分钟"%timetoWait)
	else :
		hh=timetoWait//60
		mm=timetoWait%60
		if mm==0:
			print("大约还需要等待%d小时"%hh)
		else:
			print("大约还需要等待%d小时%d分钟"%(hh,mm))
	nowtime=strftime("%Y-%m-%d %H:%M:%S")
	print('打印时间:%s'%nowtime)
	print('---------------------------------------')


if __name__=='__main__':
	# checkDb()
	while(cmd.lower()!='9' and cmd.lower()!='quit'):
		print()
		print("============Select Your Service============")
		print("1--客户取号")
		print("3--办理叫号")
		print("6--查看排队")
		print("8--我的进度")
		print("9--退出系统")
		print("===========================================")
		cmd=input()
		if cmd=='1':
			getNO()
			print('当前有%d人在排队'%queueforMeal.size())
			print()
		elif cmd=='3':
			if queueforMeal.size()>0:
				print('请输入办理密码:')
				pwd=input()
				if pwd.lower()=='admin':
					print('办理中，请稍候...')
					queueforMeal.deque()
				else:
					print('授权码错误，无法办理')				
			else:
				print('当前无人排队')
		elif cmd=='6':
			personInque=queueforMeal.size()
			if personInque<5:
				print('---喝杯茶放松下---')
				print('当前有%d人在排队'%personInque)
			elif personInque>5 and personInque <20:
				print('---赶紧得速度起来---')
				print('可怜，当前还有%d人在排队'%personInque)
			else:
				print('---该发信号弹请求支援了---')
				print('我靠，当前竟然有%d人在排队'%personInque)
		elif cmd=='8':
			print('请输出你的票号')
			yourNO=input()
			if yourNO.isdigit():
				yourNO=int(yourNO)
				if yourNO<=getPresentNO() and yourNO>(getPresentNO()-queueforMeal.size()):
					aheadPerson=queueforMeal.size()-(getPresentNO()-yourNO)-1
					print('你前面还有%d人'%aheadPerson)
				elif yourNO<=(getPresentNO()-queueforMeal.size()) and yourNO>=1:
					print('已经过号了，请重新取号')
				else:
					print('输入的票号不存在，返回重新输入')
			else:
				print('输入的票号不存在，返回重新输入')
		elif cmd=='9':
			print('已退出系统')
			break
		else:
			print('没有找到你所需要的服务,返回重新选择')




