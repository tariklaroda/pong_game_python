
# Ping-Pong Game using the turtle module.
# Done by Tarik LaRoda.
# Assignment 8
# Using Python 3
# Microsoft/VisualStudioCode/Turtle/Python3


import turtle


# Create Game Window
wind = turtle.Screen()
wind.title('pong game')
wind.bgcolor('blue')
wind.setup(width=800, height=600)
wind.tracer(0)

# Create The Player Bar A,
bar_A = turtle.Turtle()
bar_A.shape('square')
bar_A.color('white')
bar_A.shapesize(stretch_wid=5, stretch_len=1)
bar_A.penup()
bar_A.goto(-350, 0)

# Create The Computer/Player2 Bar B
bar_B = turtle.Turtle()
bar_B.shape('square')
bar_B.color('white')
bar_B.shapesize(stretch_wid=5, stretch_len=1)
bar_B.penup()
bar_B.goto(350, 0)

# Create the Pong Ball
ball = turtle.Turtle()
ball.shape('circle')
ball.color('white')
ball.penup()
ball.goto(0, 0)

# Create the pong ball's initial horizontal speed and vertical speed
ball_x = 0.1
ball_y = 0.1


# Create the score section, this keeps track of each player's points
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
    """ This function moves the Player Bar A UP"""
    y = bar_A.ycor()
    y += 30
    bar_A.sety(y)


def bar_A_down():
    """ This function moves the Player Bar A DOWN"""
    y = bar_A.ycor()
    y -= 30
    bar_A.sety(y)


# Keyboard bindings
wind.listen()
wind.onkeypress(bar_A_up, 'w')
wind.onkeypress(bar_A_down, 's')


while True:
    wind.update()

    # ball Movement
    ball.setx(ball.xcor() + ball_x)
    ball.sety(ball.ycor() + ball_y)

    # Conditions that ensure the ball bounces correctly once hitting the border
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

    # Allocate relevant score, when pong ball passes a certain point
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
    # Once a certain score is achieved, the scores restart.
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
