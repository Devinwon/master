'''
lettersGuessed: list, what letters have been guessed so far
returns: string, comprised of letters that represents what letters have not
  yet been guessed.
  注意集合的应用，需要转换成集合先
  ''.join()的是使用
'''
# FILL IN YOUR CODE HERE...
def getAvailableLetters(lettersGuessed):
    allletters=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    rel=list(set(allletters)-set(lettersGuessed))
    rel.sort()
    return ''.join(rel)

print(getAvailableLetters(['e', 'i', 'k', 'p', 'r', 's']))
