import turtle
def round_rectangle(length,high,cor_angle,cor_rad):  
      
    for i in range(2):  
        turtle.fd(high)  
        turtle.circle(cor_rad,cor_angle)  
        turtle.fd(length)  
        turtle.circle(cor_rad,cor_angle)        
      
def main2():  
    turtle.setup(1300,800,0,0)#启动窗口的大小，左上角右上角坐标  
    pythonsize=2  
    turtle.pensize(pythonsize)#运行宽度  
    turtle.speed(10)  
    turtle.seth(90)#启动时运行的方向（角度）  
      
    #最外边框  
    turtle.pencolor("#8E8e8e")  
    turtle.penup()    
    turtle.goto(202,-202)  
    turtle.pendown()  
    round_rectangle(244,484,90,30)  
    #填充  
    turtle.penup()    
    turtle.goto(200,-200)  
    turtle.pendown()  
    turtle.begin_fill()  
    turtle.color("#F0F0F0")  
    round_rectangle(240,480,90,30)  
    turtle.end_fill()  
      
    #手机屏  
    turtle.pencolor("black")#（#3000440）  
    turtle.penup()    
    turtle.goto(185,-150)  
    turtle.pendown()  
    turtle.begin_fill()  
    turtle.color("black")  
    round_rectangle(270,380,90,0)  
    turtle.end_fill()  
  
    #听筒  
    turtle.penup()    
    turtle.goto(80,265)  
    turtle.pendown()  
    turtle.begin_fill()  
    turtle.color("#9d9d9d")  
    round_rectangle(60,4,90,1)  
    turtle.end_fill()  
  
     #听筒上面的小黑  
    turtle.penup()    
    turtle.goto(67,290)  
    turtle.pendown()  
    turtle.begin_fill()  
    turtle.color("#3c3c3c")  
    round_rectangle(36,4,90,1)  
    turtle.end_fill()  
     
    #摄像头    
    turtle.penup()    
    turtle.goto(0,265)  
    turtle.pendown()  
    turtle.begin_fill()  
    turtle.color("#3c3c3c")  
    turtle.circle(6,360)  
    turtle.end_fill()  
    
  
    #home健  
    turtle.pencolor("#9d9d9d")#（#3000440）  
    turtle.penup()    
    turtle.goto(75,-185)  
    turtle.pendown()  
    turtle.circle(25,360)  
      
  
     #home健图案  
    turtle.pencolor("#9d9d9d")#（#3000440）  
    turtle.penup()    
    turtle.goto(60,-190)  
    turtle.pendown()      
    draw(10,10,90,5)  
      
main2()  
turtle.done()