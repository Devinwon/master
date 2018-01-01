'''
根据用户的提示大或者小来猜测用户'心想'(0-100范围)的那个数
'''

secret_num=int(input("Please think of a number between 0 and 100!"))
low=0
hight=100
mid=(low+hight)//2
while True:
	print("Is your secret number %d?"%mid)
	print("Enter 'h' to indicate the guess is too high.Enter 'l' to indicate the guess is too low.Enter 'c' to indicate I guessed correctly. ",end='')
	s=input()
	if s=='c':
		print("Game over. Your secret number was: %d"%mid)
		break	
	elif s=='h':
		hight=mid
	elif s=='l':
		low=mid
	else:
		print("Sorry, I did not understand your input.")
	mid=(low+hight)//2


	