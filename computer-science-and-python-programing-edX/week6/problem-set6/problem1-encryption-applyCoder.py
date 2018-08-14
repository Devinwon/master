def applyCoder(text, coder):
    """
    Applies the coder to the text. Returns the encoded text.

    text: string
    coder: dict with mappings of characters to shifted characters
    returns: text after mapping coder chars to original text
    """
    ### TODO
    finalText=""
    for v in text:
        if v.isalpha():
            finalText+=coder[v]
        else:
            finalText+=v
    return finalText
