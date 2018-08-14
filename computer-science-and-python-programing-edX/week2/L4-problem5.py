def clip(lo, x, hi):
    '''
    Takes in three numbers and returns a value based on the value of x.
    Returns:
     - lo, when x < lo
     - hi, when x > hi
     - x, otherwise
    '''
    # Your code here
    return eval("%.2f"%((lo+hi+x)-min(lo,hi,x)-max(lo,hi,x)))

print clip(-5.03, -5.68, 1.59)
