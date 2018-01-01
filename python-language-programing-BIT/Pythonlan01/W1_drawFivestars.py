from turtle import *
#import turtle
fillcolor("red")
begin_fill()
while True:
    forward(300)
    right(144)
    if abs(pos())<1:
        break

done()
#turtle.done()
#input('wait to stop')