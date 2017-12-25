for i in range(1,10):
    cnt=0
    for j in range(1,i+1):
        print(j,'*',i,'=',i*j,end=' ',sep='')
        cnt+=1
        if(cnt==i):
            print("\n")
            