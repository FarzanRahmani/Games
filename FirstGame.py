import turtle
import math
fery = turtle.Turtle()

#target
fery.pensize(5)
fery.pencolor("red")
fery.penup()
fery.goto(335,-300)
fery.pendown()
fery.fd(20)
fery.left(90)
fery.fd(16)
fery.left(90)
fery.fd(40)
fery.left(90)
fery.fd(16)
fery.left(90)
fery.fd(20)
fery.penup()

#throwing area
fery.pencolor("blue")
fery.goto(-350,-300)
fery.pendown()
fery.fd(14)
fery.left(90)
fery.fd(18)
fery.left(90)
fery.fd(7)
fery.right(90)
fery.fd(4)
fery.right(90)
fery.circle(5)
fery.right(90)
fery.fd(4)
fery.right(90)
fery.fd(7)
fery.left(90)
fery.fd(18)
fery.seth(0)
fery.penup()
fery.setpos(-343,-291)
fery.pendown()

#throwing turtle format
fery.pensize(2)
fery.pencolor("black")

def throw(t=fery,vel=0,angle=0):
    t.left(angle)
    g = -9.8
    x_0 = -343.0
    y_0 = -291.0
    time = 0.00
    for i in range(1000):
        v_x = vel*math.cos(angle*(math.pi)/180)
        v_y = g*time + vel*math.sin(angle*(math.pi)/180)
        x = v_x*time + x_0
        y = 0.5*(g)*(time**2) + v_y*time + y_0
        if 315<x<355 and -300<y<-284:
            print("you won")
            return True
        if y < -300 :
            print("try again")
            return False
        t.setpos(x,y)
        time = time + 0.01
    return False

fery.speed(0)
boolean = False
while boolean == False:
    input_angle = float(input("Please enter an angle: " ))
    input_velocity = float(input("Please enter a velocity: "))
    boolean = throw(fery,input_velocity,input_angle)
    if boolean == True:
        turtle.mainloop()
        break
    fery.up()
    fery.goto(-343,-291)
    fery.pendown()




