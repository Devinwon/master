#-*- coding:utf-8 -*-

while True:
    try:
        strlib=[]
        strcnt=int(input())
        for index in range(strcnt):
            strlib.append(input())
            
        stritem=[]
        itemcnt=int(input())
        for index in range(itemcnt):
            stritem.append(input())
        
        for v_item in stritem:
            count=0
            for v_lib in strlib:
                if v_item in v_lib:
                    count+=1
            print(count)

    except:
        break