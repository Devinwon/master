def myLog(x, b):
    '''
    x: a positive integer
    b: a positive integer; b >= 2

    returns: log_b(x), or, the logarithm of x relative to a base b.
    '''
    # Your Code Here
    t=0
    while True:
    	if b**t>x:
    		break
    	else:
    		t+=1
    return t-1

print(myLog(15,3))