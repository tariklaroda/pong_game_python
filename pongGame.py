# Tarik LaRoda A00440772
# Assignment 8
# Using Python 3
# Microsoft/VisualStudioCode/Turtle/Python3

import turtle


# Window
wind = turtle.Screen()
wind.title('pong game')
wind.bgcolor('blue')
wind.setup(width=800, height=600)
wind.tracer(0)

# Bar A
bar_A = turtle.Turtle()
bar_A.shape('square')
bar_A.color('white')
bar_A.shapesize(stretch_wid=5, stretch_len=1)
bar_A.penup()
bar_A.goto(-350, 0)

# Bar B
bar_B = turtle.Turtle()
bar_B.shape('square')
bar_B.color('white')
bar_B.shapesize(stretch_wid=5, stretch_len=1)
bar_B.penup()
bar_B.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.shape('circle')
ball.color('white')
ball.penup()
ball.goto(0, 0)
ball_x = 0.1
ball_y = 0.1


# score
sboard = turtle.Turtle()
sboard.shape('square')
sboard.color('white')
sboard.penup()
sboard.hideturtle()
sboard.goto(0, 260)

sboard.write("Player A: 0 Player B: 0", align="center",
             font=("Courier", 24, 'normal'))
score_a = 0
score_b = 0
# functions


def bar_A_up():
    y = bar_A.ycor()
    y += 30
    bar_A.sety(y)


def bar_A_down():
    y = bar_A.ycor()
    y -= 30
    bar_A.sety(y)


# Keyboard bindings
wind.listen()
wind.onkeypress(bar_A_up, 'w')
wind.onkeypress(bar_A_down, 's')
# wind.onkeypress(bar_B_up, 'Up')
# wind.onkeypress(bar_B_down, 'Down')


while True:
    wind.update()

    # ball Movement
    ball.setx(ball.xcor() + ball_x)
    ball.sety(ball.ycor() + ball_y)

    # Border
    if ball.ycor() > 290:
        ball.sety(290)
        ball_y *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball_y *= -1

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball_x *= -1
        score_a += 1

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball_x *= -1
        score_b += 1

    # score
    if ball.xcor() > 350:
        score_a += 1
        sboard.clear()
        sboard.write("Player A: {} Player B: {}".format(
            score_a, score_b), align='center', font=("Courier", 24, 'normal'))
        ball.goto(0, 0)
        ball_x *= -1
    elif ball.xcor() < -350:
        score_b += 1
        sboard.clear()
        sboard.write("Player A: {} Player B: {}".format(
            score_a, score_b), align='center', font=("Courier", 24, 'normal'))
        ball.goto(0, 0)
        ball_x *= -1

    # End game conditions
    if score_a > 4 or score_b > 4:
        score_a = 0
        score_b = 0

    # Bar B follows ball
    bar_B.sety(ball.ycor())

    # Collision with bars
    if ball.xcor() < -340 and ball.ycor() < bar_A.ycor() + 50 and ball.ycor() > bar_A.ycor() - 50:
        ball_x *= -1
    elif ball.xcor() > 340 and ball.ycor() < bar_B.ycor() + 50 and ball.ycor() > bar_B.ycor() - 50:
        ball_x *= -1
