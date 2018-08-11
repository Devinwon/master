def buildCoder(shift):
    """
    Returns a dict that can apply a Caesar cipher to a letter.
    The cipher is defined by the shift value. Ignores non-letter characters
    like punctuation, numbers and spaces.

    shift: 0 <= int < 26
    returns: dict
    """
    ### TODO.
    # return "Not yet implemented." # Remove this comment when you code the function
    dic={}
    lcase="abcdefghijklmnopqrstuvwxyz"
    ucase="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for l in lcase:
        dic[l]=chr((ord(l)+shift-97)%26+ord('a'))
    for u in ucase:
        dic[u]=chr((ord(u)+shift-65)%26+ord('A'))
    return dic

def applyShift(text, shift):
    """
    Given a text, returns a new text Caesar shifted by the given shift
    offset. Lower case letters should remain lower case, upper case
    letters should remain upper case, and all other punctuation should
    stay as it is.

    text: string to apply the shift to
    shift: amount to shift the text (0 <= int < 26)
    returns: text after being shifted by specified amount.
    """
    ### TODO.
    ### HINT: This is a wrapper function.
    # return "Not yet implemented." # Remove this comment when you code the function
    afterText=""
    for c in text:
        if c.isalpha():
            afterText+=buildCoder(shift)[c]
        else:
            afterText+=c 
    return afterText
    
print applyShift('This is a test.', 8)
print applyShift('Bpqa qa i bmab.', 18)