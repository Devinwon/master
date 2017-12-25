# 两只乒乓球队比赛，每队各出三人
# 甲队为a,b,c三人，已队为x,y,z三人，已抽签决定比赛名单
# 有人向队员打听比赛的名单，
# a不和x比
# c不和x ,z比赛，编写程序找出三队赛手的名单
teama=['a','b','c']
teamx=['x','y','z']
for ta in teama:
    if(ta=='c'):
        temp=teamx[:]
        temp.remove('x')
        temp.remove('z')
        print(ta+":"+temp[0])
        teama.remove(ta)
        #teama=['a','b']
        for tx in teamx:
            if(tx==temp[0]):
                teamx.remove(temp[0])
                # teamx=[x,z]

for ta in teama:
    if(ta=='a'):
        for tx in teamx:
            if(tx!='x'):
                print(ta+":"+tx)
                teama.remove(ta)
                teamx.remove(tx)
                
print(teama[0]+":"+teamx[0])
