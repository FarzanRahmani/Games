import turtle 
import random
import math

turtle.colormode(255)
def set_random_color(t):
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    t.color(r, g, b)


def set_scr():
    win = turtle.Screen()
    win.bgcolor("black")
    win.title("Farzan's paddle")
    win.setup(width=800,height=800)
    return win
win = set_scr()


def f_paddle():
    paddle = turtle.Turtle()
    paddle.shape("square")
    paddle.shapesize(1,5)
    paddle.color("blue")
    paddle.penup()
    paddle.goto(0,-350)
    return paddle
paddle = f_paddle()

targets = []
def target(y_cor):
    for i in range(15):
        x = str(i)
        x = turtle.Turtle()
        x.speed(0)
        x.penup()
        x.shape("square")
        set_random_color(x)
        x.shapesize(1,2)
        if i <= 14 :
            x.setpos(350-(50*i),y_cor)
            targets.append(x)

target(350)
target(325)
target(300)
target(275)

def f_ball():
    ball = turtle.Turtle()
    ball.penup()
    ball.color("red")
    ball.shape("circle")
    ball.shapesize(.5,.5)
    ball.setpos(0,-330)
    return ball
ball = f_ball()

def go_right():
    x = paddle.xcor()
    paddle.setx(x+30)
    return paddle

def go_left():
    x = paddle.xcor()
    paddle.setx(x-30)
    return paddle

def keyboard_listen():
    win.listen()
    win.onkey(go_right, "Right")
    win.onkey(go_left, "Left")
    return win
keyboard_listen()


def ran_angle():
    theta = random.randint(30,150)
    theta = theta*(math.pi/180)
    return theta
zavie = ran_angle()

v_x = 0
v_y = 0

def sorat_avalie(x):
    global v_x
    global v_y
    v = x
    v_x = v*math.cos(zavie)
    v_y = v*math.sin(zavie)
sorat_avalie(30)

def move_ball(toop):
    global v_x
    global v_y
    t= 0.1
    x_0 , y_0 = ball.position()
    ball.goto(x_0+v_x*t , y_0+v_y*t)
    return toop

def border_collision():
    global v_x
    global v_y
    x , y = ball.position()
    if x > 400 :
        v_x = -1*v_x
    if x < -400 :
        v_x = -1*v_x
    if y > 400 :
        v_y = -1*v_y

def paddle_collision():
    global v_y
    global v_x
    x_0 , y_0 = paddle.position()
    x , y = ball.position()
    if (x_0-55 < x) and (x < x_0+55) and (y_0 -15 < y) and (y < y_0 +15):
        v_y = -1*v_y
        if (x < x_0 - 29) and (v_x > 0) :
            v_x = -1*v_x
        if (x > x_0 + 29) and (v_x < 0) :
            v_x = -1*v_x

def targets_collsion():
    global targets
    global v_y
    global v_x
    global score
    global high_score
    for t in targets:
        if ball.distance(t) < 23 :
            if v_x > 0:
                v_x = v_x + 5
            if v_x < 0:
                v_x = v_x - 5
            if v_y > 0 :
                v_y = v_y + 5
            if v_y < 0 :
                v_y = v_y - 5
            t.setpos(2000,2000)
            v_y = v_y*(-1)
            score += 5
            if score > high_score:
                high_score = score
            update_score()

def gameover():
    global score
    global targets
    global zavie
    if ball.ycor() < -400 :
        paddle.goto(0,-350)
        ball.setpos(0,-330)
        zavie = ran_angle()
        sorat_avalie(30)
        score = 0
        update_score()
        for t in targets:
            t.setpos(2000,2000)
        targets.clear()
        target(350)
        target(325)
        target(300)
        target(275)

def score_turtle():
    # score turtle
    pen = turtle.Turtle()
    pen.speed(0)
    pen.shape("square")
    pen.color("white")
    pen.penup()
    pen.hideturtle()
    pen.goto(0,365)
    pen.write("Score: {} High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))
    return pen
score = 0 
high_score = 0
pen = score_turtle()

def update_score():
    pen.clear()
    pen.write("Score: {} High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))

while True:
    move_ball(ball)
    border_collision()
    paddle_collision()
    targets_collsion()
    gameover()
