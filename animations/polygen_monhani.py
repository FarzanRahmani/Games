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


def polygen_monhani(l,t,n):
    """  l=length  t=turtle   n=tedad azla"""
    t.penup()
    t.setpos(-l/2,-l/2)
    t.seth(90)
    t.pendown()
    j = 1
    for i in range(l,1,-1):
        t.forward(i)
        t.right(360/n)
        if j % n == 0 :
            set_random_color(t)
        j = j +1

polygen_monhani(100,ab,20)

turtle.mainloop()