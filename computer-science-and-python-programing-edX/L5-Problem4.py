def gcdIter(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    # Your code here
    minof=min(a,b)
    maxof=max(a,b)
    while minof:
        i=minof
        minof=min(minof,maxof%minof)
        maxof=i
    return maxof