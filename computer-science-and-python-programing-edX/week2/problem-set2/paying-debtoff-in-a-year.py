balance=3926
annualInterestRate=0.2

monInterestRate=annualInterestRate/12.0
payment=10
while True:
	mybalance=balance
	for _ in range(12):
		unpaidBlance=mybalance-payment    #欠款
		interest=unpaidBlance*monInterestRate	#利息
		mybalance=unpaidBlance+interest #更新欠款
	#一年后,比较欠款
		# print("unpaidBlance",unpaidBlance)

	if unpaidBlance<=0:
		break
	else:
		payment+=10

print(payment)

