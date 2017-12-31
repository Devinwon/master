import random
import time
namelist=['张三','网商','华德','学友','雪亮','雪莲','丛丛','devin','jeson','green']
prize_item={'一等奖':1,"二等奖":2,"三等奖":3}

nmlist=namelist[:]
user_gotprize=[]

for cnt in range(6):
	# r=int(random.random()*10)%len(namelist)
	r=random.randint(0,len(namelist)-1)
	time.sleep(3)
	print(namelist.pop(r))