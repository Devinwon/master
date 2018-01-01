#print("我是谁")
diet=['西红柿','黄瓜','洋葱','土豆','辣椒']
sn=0
for x in range(0,5):
    for y in range(x+1,5):
        if not(x==y):
            sn=sn+1
            print(sn,"{} {}".format(diet[x],diet[y]))
