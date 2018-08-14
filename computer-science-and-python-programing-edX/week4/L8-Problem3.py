#define the SimpleDivide function here
def SimpleDivide(item, denom):
    try:
        t=item/denom
    except ZeroDivisionError:
        t=0
    return t     