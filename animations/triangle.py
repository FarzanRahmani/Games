import turtle
import random
import math

F = turtle.Turtle()
F.pensize(3)
turtle.colormode(255) 

wh = turtle.Screen()
wh.bgcolor("black")

def st_rd_cl(t):
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    t.pencolor(r,g,b)

def triangle(t,size,step):
    t.penup()
    t.setpos(-size/2,(-1)*math.sin(math.pi/3)*size/3)
    t.pendown()
    t.seth(60)
    for i in range(size,1,-step):
        st_rd_cl(t)
        t.fd(i)
        t.right(120) #360/3 zavie khareji/n

triangle(F,200,10)
turtle.mainloop()