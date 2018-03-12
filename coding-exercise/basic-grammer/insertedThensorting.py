# insertedThensorting.py
olst=[10,23,45,67,100]
print("Before:",olst)
intnum=int(input("Input a new number:"))

for i in range(len(olst)-1):
    if(olst[i]<=intnum<olst[i+1]):
        olst.insert(i+1,intnum)
        break
    else:
        if(intnum<olst[0]):
            olst.insert(0,intnum)
            break
        elif(intnum>=olst[-1]):
            olst.append(intnum)
            break


print("After:",olst)

for i in range(len(olst)):
    print(olst[len(olst)-(i+1)],' ',end='')
print('')
