import turtle
import random
import math

wh = turtle.Screen()
wh.bgcolor("black")
turtle.colormode(255)
fer = turtle.Turtle()

def init(): #initialize
    john = turlte.Turtle()
    turtle.colormode(255)
    john.pensize(3)
    john.speed(0)
    return john

def set_random_color(t):
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    t.pencolor(r, g, b)


def halazoon(t,r):
    t.penup()
    t.setpos(r,0)
    t.pendown()
    t.pensize(3)
    t.speed(0)
    for d in range(360*8):
        x = r*math.cos(d*(math.pi/180))
        y = r*math.sin(d*(math.pi/180))
        t.setpos(x,y)
        r = r/1.0008 #ziba tar az r = r-0.01   r*0.999
        if d%360==0:
            set_random_color(t)

halazoon(fer,150)
turtle.mainloop()
