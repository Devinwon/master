'''
螺旋的绘制
'''
import turtle

turtle.bgcolor("black")
colors=["#008792","#b2d235","#6f60aa","#f58f98","#ed1941","orange","purple","green"]
for x in range(10,80):
	turtle.color(colors[x%len(colors[:3])])
	turtle.circle(x)	
	turtle.left(121)
turtle.done()