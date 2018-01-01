# def odd(x):
# 	return bool(x%2) 

# print(odd(3))
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
    return eval('%.2f'%rel)

print(iterPower(2,3))