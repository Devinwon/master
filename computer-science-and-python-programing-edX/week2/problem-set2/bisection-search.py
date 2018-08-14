# coding:UTF-8
balance = 999999
annualInterestRate = 0.18

monthlyRate=annualInterestRate/12.0
lo=balance/12.0
hi=(balance*(1+monthlyRate)**12)/12.0
while lo<hi:
	payment=(lo+hi)/2.0
	mybalance=balance
	for m in range(12):
		unpaidBlance=mybalance-payment  #欠款
		interest=unpaidBlance*monthlyRate #产生利息
		mybalance=unpaidBlance+interest
	if -0.001<=unpaidBlance<=0.001 :
		break  #求出结果，退出循环
	elif unpaidBlance>0.001:
		lo=payment
	elif unpaidBlance<-0.001:
		hi=payment

print "Lowest Payment: {:0.2f}".format(payment)