# 系统评判的问题,无法评判

def jumpAndBackpedal(isMyNumber):
	guess = 1
	foundNumber = False
	while not foundNumber:
		sign=isMyNumber(guess)
		if sign == 0:
			foundNumber=True
		elif sign==-1
			guess *= 2
		elif sign==1:
			guess -= 1
	return guess