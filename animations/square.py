import turtle
import random
import math

ab = turtle.Turtle()
turtle.colormode(255)

def set_random_color(t):
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    t.pencolor(r, g, b)



def square(size,t,step):
    t.penup()
    t.goto(-1*size/2,-1*size/2)
    t.seth(90)
    t.pendown()
    for i in range(size,1,-step):
        set_random_color(t)
        t.forward(i)
        t.right(90)

square(250,ab,10)

def square1(l,t):
    t.penup()
    t.setpos(-l/2,-l/2)
    t.seth(90)
    t.pendown()
    j = 1
    for i in range(l,1,-10):
        t.forward(i)
        t.right(90)
        if j % 4 == 0 :
            set_random_color(t)
        j = j +1

square1(150,ab)

turtle.mainloop()