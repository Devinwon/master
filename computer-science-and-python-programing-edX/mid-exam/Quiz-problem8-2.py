def sqrt(a):
    def tryit(x):
        return 0.5 * (a/x + x)
    # return fixedPoint(tryit(a), 0.0001)  #bug
    return fixedPoint(tryit, 0.0001)       # corrected