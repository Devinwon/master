# Paste your code into this box
#secret_num=int(raw_input("Please think of a number between 0 and 100!"))
print("Please think of a number between 0 and 100!")
low=0
hight=100
mid=(low+hight)//2
while True:
    print( "Is your secret number %d?"%mid)
    print "Enter 'h' to indicate the guess is too high.Enter 'l' to indicate the guess is too low.Enter 'c' to indicate I guessed correctly.",
    s=raw_input()
    if s=='c':
        print( "Game over. Your secret number was: %d"%mid)
        break
    elif s=='h':
        hight=mid
    elif s=='l':
        low=mid
    else:
        print ("Sorry, I did not understand your input.")
    mid=(low+hight)//2
