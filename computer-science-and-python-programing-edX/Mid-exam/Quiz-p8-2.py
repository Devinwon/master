"""
f(x)=1/2(a/x+x)

This code has a bug in it. 
You can fix this by correcting exactly one line of the definition. 
Please do so in the box below.
"""
def fixedPoint(f, epsilon):
    """
    f: a function of one argument that returns a float
    epsilon: a small float
  
    returns the best guess when that guess is less than epsilon 
    away from f(guess) or after 100 trials, whichever comes first.
    this code 

    if f(guess) - guess < epsilon:
     
    change to 
    if abs(f(guess) - guess) < epsilon:
    
    """
    guess = 1.0
    for i in range(100):
        if abs(f(guess) - guess) < epsilon:
            return guess
        else:
            guess = f(guess)
    return guess


def sqrt(a):
    def tryit(x):
        return 0.5 * (a/x + x)
    return fixedPoint(tryit(a), 0.0001)

