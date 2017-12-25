def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    
    for c in secretWord:
        if c not in lettersGuessed:
            return False
    return True
print(isWordGuessed("apple",['e', 'i', 'k', 'p', 'r', 's']))