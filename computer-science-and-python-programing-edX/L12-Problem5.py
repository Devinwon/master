"""
def genFib():
	fibn_1 = 1 #fib(n-1)
	fibn_2 = 0 #fib(n-2)
	while True:
# fib(n) = fib(n-1) + fib(n-2)
		next = fibn_1 + fibn_2
		yield next
		fibn_2 = fibn_1
		fibn_1 = next


cnt=0

for n in genFib():
	print(n,'',end="")
	cnt+=1
	if cnt%5==0:
		print('\n')
	if cnt>10:
		break
"""
import math
def is_prime(number):
    if number > 1:
        if number == 2:
            return True
        if number % 2 == 0:
            return False
        for current in range(3, int(math.sqrt(number) + 1), 2):
            if number % current == 0: 
                return False
        return True
    return False

def genPrimes():
	n=1
	while True:
		if is_prime(n):
			yield n
		n+=1

gen=genPrimes()

cnt=0
while True:
	print gen.next()
	cnt+=1
	if cnt>10:
		break
