'''

'''
#根据 a,b 的假设三种（1，0），（0，1），（1，1）
'''
for a,b in ((1,0),(0,1),(1,1)):

    if a,b=1,0:        #假设a,b（0，1），（1，1）
        c=b             #求解c
        d=abs(c-1)      #求解d

        #验证
        if a+d==0 or a+d==1:
            pass
        else:
            break


        if d==0:
            e=0         #求解e

        #验证：
        f=2-a-e
        if f<=1:
            pass
        else:
            break

'''
'''
class Clock(object):
    def __init__(self, time):
        self.time = time
    def print_time(self):
        time = '6:30'
        print(self.time)

clock = Clock('5:30')
clock.print_time()
'''
class Clock(object):
    def __init__(self, time):
        self.time = time
    def print_time(self, time):
        print(time)

clock = Clock('5:30')
clock.print_time('10:30')

