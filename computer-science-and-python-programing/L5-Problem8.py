def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    # Your code here
    if len(aStr)<=1:
        return char==aStr
    else:
        left_index=0
        right_index=len(aStr)-1
        mid_index=(right_index+left_index)//2
        if char==aStr[mid_index]:
            return True
        elif char<aStr[mid_index]:
            return isIn(char,aStr[left_index:mid_index]) 
        else:
            return isIn(char,aStr[mid_index+1:right_index+1])

print(isIn('a',''))