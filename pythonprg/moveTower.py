step=0

def moveTower(height,fromdisk,todisk,withdisk):
	if height>=1:
		moveTower(height-1,fromdisk,withdisk,todisk)
		moveInfo(fromdisk,todisk)
		moveTower(height-1,withdisk,todisk,fromdisk)

def moveInfo(frm,to):
	# global step++
	# step=step+1
	temp=step+1
	# step=temp
	print(temp,"move disk from %s to %s"%(frm,to))

moveTower(3,'A','B','C')