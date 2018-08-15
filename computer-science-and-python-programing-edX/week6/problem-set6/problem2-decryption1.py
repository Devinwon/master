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


def findBestShift(wordList, text):
    """
    Finds a shift key that can decrypt the encoded text.

    text: string
    returns: 0 <= int < 26
    """
    ### TODO
    # return "Not yet implemented." # Remove this comment when you code the function
    key,shift=0,0
    maxValid=0 #统计解密后能识别的单词数目
    while shift<26:
        counting=0
        txtafter=applyShift(text,26-shift)
        txtafter=txtafter.split()
        for w in txtafter:
            if isWord(wordList, w):
                counting+=1
        if counting>maxValid:
            maxValid=counting                
            key=shift
        shift+=1
    return key 