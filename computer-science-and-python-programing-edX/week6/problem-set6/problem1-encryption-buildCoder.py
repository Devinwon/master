def buildCoder(shift):
    """
    Returns a dict that can apply a Caesar cipher to a letter.
    The cipher is defined by the shift value. Ignores non-letter characters
    like punctuation, numbers, and spaces.

    shift: 0 <= int < 26
    returns: dict
    """
    ### TODO
    dic={}
    lcase="abcdefghijklmnopqrstuvwxyz"
    ucase="ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    for l in lcase:
    	dic[l]=chr((ord(l)+shift-97)%26+ord('a'))
    for u in ucase:
    	dic[u]=chr((ord(u)+shift-65)%26+ord('A'))
    return dic
