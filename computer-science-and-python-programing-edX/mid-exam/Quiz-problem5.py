def laceStrings(s1, s2):
    """
    s1 and s2 are strings.

    Returns a new str with elements of s1 and s2 interlaced,
    beginning with s1. If strings are not of same length, 
    then the extra elements should appear at the end.
    """
    # Your Code Here
    commanLen=min(len(s1),len(s2))
    rel=""
    for i in range(commanLen):
    	rel+=s1[i]+s2[i]
    if len(s1)>commanLen:
    	rel+=s1[commanLen:]
    elif len(s2)>commanLen:
    	rel+=s2[commanLen:]
    return rel
print(laceStrings("",""))


