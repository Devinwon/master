from turtle import *
#import turtle
hideturtle()
#turtle.hideturtle()
'''print(sum(x for x in range(10)))'''
#color("red","yellow")
color("black","purple")#first_line,last_zone
begin_fill()
while True:
    forward(150)
    left(170)
    #right(45)#8边形
    #right(50)#
    #right(60)#6边形
    #left(90)    #正方形
    #left(120)   #等边三角形
    #left(135)   #
    if abs(pos())<1:        #封闭
        break

end_fill()
done()
