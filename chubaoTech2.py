# -*- coding: utf-8 -*-
import math
def getDis(x1,y1,x2,y2):
    return math.sqrt(abs((x1-x2))**2+abs((y1-y2))**2)

while True:
    try:
        cntofpoint=int(input())
#存储所有点的坐标及向量
        positionandspeed=[]
        for index in range(cntofpoint):
               pspd= list(input().split())
               for index in range(len(pspd)):  
                   pspd[index]=int(pspd[index])
               positionandspeed.append(pspd)
#         坐标信息正确进行了输出
#         print(positionandspeed)
        maxgap=0
        spedots=[]
        for i in range(len(positionandspeed)-1):
            for j in range(i+1,len(positionandspeed)):
                temp=getDis(positionandspeed[i][0],positionandspeed[i][1] , positionandspeed[j][0], positionandspeed[j][1])
                if temp>maxgap:
                    spedots=[]
                    spedots.append(positionandspeed[i])
                    spedots.append(positionandspeed[j])
                    maxgap=temp
#         print(spedots)
        t=(spedots[0][0]-spedots[1][0]-spedots[0][1]+spedots[1][1])/(spedots[1][2]-spedots[1][3]-spedots[0][2]+spedots[0][3])
        d=getDis(spedots[0][0]+t*spedots[0][2],spedots[0][1]+t*spedots[0][3],spedots[1][0]+t*spedots[1][2],spedots[1][1]+t*spedots[1][3],)
        print("%.2f %.2f"%(t,d))
    except:
        break
