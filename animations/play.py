import turtle

def draw_square(t,l):
    for i in range(4):
        t.forward(l)
        t.right(90)

def draw_polygon(t,l,n):
    for i in range(n):
        t.forward(l)
        t.right(360/n)

alex = turtle.Turtle() #mitooni be jaye t bezari alex

# draw_square(alex,150)
# alex.penup()
# alex.setpos(-100,100)
# alex.pendown()
# draw_polygon(alex,150,8)
alex.color("blue")
for i in range(20,130,20):
    alex.circle(i)
    alex.color("olive")

turtle.mainloop()