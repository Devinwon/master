# 6.00 Problem Set 3
# 
# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...") 
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    # wordlist = string.split(line)
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.") 
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
# wordlist = loadWords()

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



def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    replaced='_ '
    rel=""
    for v in secretWord:
        if v in lettersGuessed:
            rel+=v
        else:
            rel+=replaced
    return rel



def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    allletters=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    rel=list(set(allletters)-set(lettersGuessed))
    rel.sort()
    return ''.join(rel)
    

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE...
    print('Welcome to the game, Hangman!')
    print('I am thinking of a word that is %d letters long.'%(len(secretWord)))
    total=8
    lettersGuessed=[]
    count=0
    while True :
        print('-------------')
        if getGuessedWord(secretWord, lettersGuessed)==secretWord:
            print('Congratulations, you won!')
            break
        elif count ==total :
            print('Sorry, you ran out of guesses. The word was %s.'%secretWord)
            break
        print('You have %d guesses left.'%(total-count))
        print('Available letters: ',end='')
        print(getAvailableLetters(lettersGuessed))
        print('Please guess a letter: ',end='')

        c=input().lower()
        if c not in lettersGuessed and c in secretWord:
            lettersGuessed.append(c)
            print('Good guess: ',end='')
            print(getGuessedWord(secretWord, lettersGuessed))
        elif c in lettersGuessed :
            print("Oops! You've already guessed that letter: ",end='')
            print(getGuessedWord(secretWord, lettersGuessed))
        else:
            lettersGuessed.append(c)
            count+=1
            print('Oops! That letter is not in my word: ',end='')
            print(getGuessedWord(secretWord, lettersGuessed))






# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

wordlist=loadWords()
secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
