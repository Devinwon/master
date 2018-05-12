from ps4a import *
import time
# from __future__ import print_function
#-*- coding:utf-8 -*-

#
#
# Problem #6: Computer chooses a word
#
#
def compChooseWord(hand, wordList, n):
    """
    Given a hand and a wordList, find the word that gives 
    the maximum value score, and return it.

    This word should be calculated by considering all the words
    in the wordList.

    If no words in the wordList can be made from the hand, return None.

    hand: dictionary (string -> int)
    wordList: list (string)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)

    returns: string or None
    """
    # BEGIN PSEUDOCODE <-- Remove this comment when you code this function; do your coding within the pseudocode (leaving those comments in-place!)
    # Create a new variable to store the maximum score seen so far (initially 0)

    # Create a new variable to store the best word seen so far (initially None)  

    # For each word in the wordList

        # If you can construct the word from your hand
        # (hint: you can use isValidWord, or - since you don't really need to test if the word is in the wordList - you can make a similar function that omits that test)

            # Find out how much making that word is worth

            # If the score for that word is higher than your best score

                # Update your best score, and best word accordingly

    # submit error:calculateHandlen not defined
    SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}
    def calculateHandlen(hand):
        return sum(hand.values())
    def getWordScore(word, n):
        score=0
        if word:
            for v in word:
                score+=SCRABBLE_LETTER_VALUES[v]
            score*=len(word)
            if len(word)==n:
                score+=50
        return score
    # return the best word you found.
    maxScore=0
    bestWord=None
    for word in wordList:
        found=True
        handcpy=hand.copy()
        if len(word)<=calculateHandlen(handcpy):
            for c in word:
                if handcpy.get(c,0):
                    handcpy[c]-=1
                else:
                    found=False
                    break
            if found:
                if getWordScore(word,n)>maxScore:
                    bestWord=word
                    maxScore=getWordScore(word,n)
    return bestWord

#
# Problem #7: Computer plays a hand
#
def compPlayHand(hand, wordList, n):
    """
    Allows the computer to play the given hand, following the same procedure
    as playHand, except instead of the user choosing a word, the computer 
    chooses it.

    1) The hand is displayed.
    2) The computer chooses a word.
    3) After every valid word: the word and the score for that word is 
    displayed, the remaining letters in the hand are displayed, and the 
    computer chooses another word.
    4)  The sum of the word scores is displayed when the hand finishes.
    5)  The hand finishes when the computer has exhausted its possible
    choices (i.e. compChooseWord returns None).
 
    hand: dictionary (string -> int)
    wordList: list (string)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)
    """
    # TO DO ... <-- Remove this comment when you code this function
    total=0
    while calculateHandlen(hand):
        print "Current Hand:",
        displayHand(hand)
        bestWord=compChooseWord(hand, wordList, n)
        if bestWord:
            score=getWordScore(bestWord,n)
            total+=score
            hand=updateHand(hand, bestWord)
            print '"%s" earned %d points. Total: %d points'%(bestWord,score,total)
            # print '"{}" earned {} points. Total: {} points'.format(bestWord,score,total)
        else:
           break 
        if not calculateHandlen(hand) :
            print 
    print "Total score: {} points.".format(total)
    print

    
#
            # hand renew
# Problem #8: Playing a game
#
#
def playGame(wordList):
    """
    Allow the user to play an arbitrary number of hands.
 
    1) Asks the user to input 'n' or 'r' or 'e'.
        * If the user inputs 'e', immediately exit the game.
        * If the user inputs anything that's not 'n', 'r', or 'e', keep asking them again.

    2) Asks the user to input a 'u' or a 'c'.
        * If the user inputs anything that's not 'c' or 'u', keep asking them again.

    3) Switch functionality based on the above choices:
        * If the user inputted 'n', play a new (random) hand.
        * Else, if the user inputted 'r', play the last hand again.
      
        * If the user inputted 'u', let the user play the game
          with the selected hand, using playHand.
        * If the user inputted 'c', let the computer play the 
          game with the selected hand, using compPlayHand.

    4) After the computer or user has played the hand, repeat from step 1

    wordList: list (string)
    """
    # TO DO... <-- Remove this comment when you code this function
    # print "playGame not yet implemented." # <-- Remove this when you code this function
    last=''
    while True:
        print "Enter n to deal a new hand, r to replay the last hand, or e to end game:",
        cmd=raw_input()
        if cmd.lower()=='n' or cmd.lower()=='r':
            print 
            while True:
                print "Enter u to have yourself play, c to have the computer play:",
                playmod=raw_input()
                if playmod=='u':
                    print 
                    if cmd.lower()=='r':
                        playHand(last, wordList, HAND_SIZE)
                        break
                    else:
                        hand=dealHand(HAND_SIZE)
                        last=hand.copy()
                        playHand(hand, wordList, HAND_SIZE)
                        break
                elif playmod=='c':
                    print
                    if cmd.lower()=='r':
                        compPlayHand(last, wordList, HAND_SIZE)
                        break
                    else:
                        hand=dealHand(HAND_SIZE)
                        last=hand.copy()
                        compPlayHand(hand, wordList, HAND_SIZE)
                        break
                else:
                    print "Invalid command."
                    print 
                

        elif cmd.lower()=='e':
            break
        else:
            print "Invalid command."
            print 




#
# Build data structures used for entire session and play game
#
if __name__ == '__main__':
    wordList = loadWords()
    # hand={'a': 1, 'p': 2, 's': 1, 'e': 1, 'l': 1}
    # hand={'a': 2, 'c': 1, 'b': 1, 't': 1}
    # hand={'a': 2, 'e': 2, 'i': 2, 'm': 2, 'n': 2, 't': 2}
    # compChooseWord(hand, wordList, 6)
    # print("final",compChooseWord(hand, wordList, 6))
    # compPlayHand(hand, wordList, 12)
    # print(compChooseWord({'x': 2, 'z': 2, 'q': 2, 'n': 2, 't': 2}, wordList, 12))
    playGame(wordList)
    # compPlayHand({'a': 2, 'e': 2, 'i': 2, 'm': 2, 'n': 2, 't': 2}, wordList, 12)

