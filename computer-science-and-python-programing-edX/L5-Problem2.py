'''
Your code must be recursive - 
use of the ** operator or looping constructs is not allowed.
'''
def recurPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    # Your code here
    # rel=1
    if exp==0:
        rel=1
    elif exp==1:
        rel=base
    else:
        rel=base*recurPower(base,exp-1)
    return rel
print(recurPower(2,10))