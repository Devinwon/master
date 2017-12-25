chr=(input("Input one char:"))
# print(chr)
# Mon,,Wed,Fri,Tue,Thu,Sat,Sun
if(chr=='m' or chr=='M'):
    print("It’s Monday")
elif(chr=='w' or chr=='W'):
    print("It’s Wednesday")
elif(chr=='f' or chr=='F'):
    print("It’s Friday")
elif(chr=='t' or chr=='T'):
    chr=(input("need to input the second char:"))
    if(chr=='u' or chr=='U'):
        print("It’s Tuesday")
    elif(chr=='h' or chr=='H'):
        print("It’s Thursday")
    else:
        print("Error")

elif(chr=='s' or chr=='S'):
    chr=(input("need to input the second char:"))
    if(chr=='a' or chr=='A'):
        print("It’s Saturday")
    elif(chr=='u' or chr=='U'):
        print("It’s Sunday")
    else:
        print("Error")
else:
    print("Error")
