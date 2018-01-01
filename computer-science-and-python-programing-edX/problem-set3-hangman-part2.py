'''
secretWord: string, the word the user is guessing
lettersGuessed: list, what letters have been guessed so far
returns: string, comprised of letters and underscores that represents
  what letters in secretWord have been guessed so far.
'''
# FILL IN YOUR CODE HERE...
def getGuessedWord(secretWord, lettersGuessed):
    replaced='_ '
    rel=""
    for v in secretWord:
        if v in lettersGuessed:
            rel+=v
        else:
            rel+=replaced
    return rel
print(getGuessedWord(('apple'),['e', 'i', 'k', 'p', 'r', 's']))



