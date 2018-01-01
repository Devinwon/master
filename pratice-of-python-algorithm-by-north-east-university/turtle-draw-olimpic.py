'''
奥运五环的绘制
'''

import turtle
psize=5
r=45
turtle.pensize(psize)
turtle.color("blue")
turtle.penup()
turtle.goto(-110,-25)
turtle.pendown()
turtle.circle(r)

turtle.color("black")
turtle.penup()
turtle.goto(0,-25)
turtle.pendown()
turtle.circle(r)

turtle.color("red")
turtle.penup()
turtle.goto(110,-25)
turtle.pendown()
turtle.circle(r)

turtle.color("yellow")
turtle.penup()
turtle.goto(-55,-75)
turtle.pendown()
turtle.circle(r)

turtle.color("green")
turtle.penup()
turtle.goto(55,-75)
turtle.pendown()
turtle.circle(r)

turtle.done()