'''
Your code must be recursive - 
use of the ** operator or looping constructs is not allowed.
Notice:equal replacement
'''
def recurPowerNew(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    # Your code here
    # rel=1
    if exp==0:
        rel=1
    elif exp>0:
        if exp%2==0:
            # even
            # rel=(base*base)**(exp/2)
            rel=recurPowerNew(base*base,exp/2)
        else:
            # odd 
            rel=base*recurPowerNew(base,exp-1)
    else:
        rel='argument exp shoud >0'
    return rel
print(recurPowerNew(2,10))
