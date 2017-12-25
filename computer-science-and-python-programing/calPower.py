    '''
    base: int or float.
    exp: int >= 0
    returns: int or float, base^exp,couldn't use **operator
    '''
def iterPower(base,exp):
    rel=base
    if exp==0:
    	rel=1
    elif exp==1:
    	pass
    else:
    	while exp>=2:
          rel=base*rel
          exp=exp-1
    return rel

print(iterPower(2,3))
