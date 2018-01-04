
import random,time

# list can keep the order
# 奖项类别以及人数设置
# 简单的人员存储在列表当中
prize_item=[["三等奖",3],["二等奖",2],["一等奖",1]]
user=["devin","bob","matina","jesson","hank","frank","green","white","blue","natting","kin","jon"]

# user_bak=user[:]
def contest(user,prize_item):
	lucky_dog=[]
	print("\n下面开始抽奖，请保持关注\n")
	for v in prize_item:
		time.sleep(2)
		print("\n开始抽取"+v[0]+"......\n")
		for cnt in range(v[1]):
			time.sleep(2)
			nm=user.pop(random.randint(0,len(user)-1))
			lucky_dog.append(nm) 
			print("恭喜"+v[0]+"获得者："+nm)

	print("\n恭喜以上"+str(len(lucky_dog))+"位获奖者")

contest(user,prize_item)