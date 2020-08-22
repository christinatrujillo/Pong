#Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:43:08) [MSC v.1926 32 bit (Intel)] on win32
#Type "help", "copyright", "credits" or "license()" for more information.

import turtle

wn = turtle.Screen()
wn.title("Pong")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# score
score_a = 0
score_b = 0

# Paddle A
# paddle_a = name; turtle = module name; Turtle = class name
paddle_a = turtle.Turtle()
paddle_a.speed(0)  #speed of animation to max possible speed
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1) #stretches the size of the paddle
paddle_a.penup() #draw a line
paddle_a.goto(-350, 0)  #this is the location that the paddle starts on screen

# Paddle B
# paddle_b = name; turtle = module name; Turtle = class name
paddle_b = turtle.Turtle()
paddle_b.speed(0)  #speed of animation to max possible speed
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1) #stretches the size of the paddle
paddle_b.penup() #draw a line
paddle_b.goto(+350, 0)  #this is the location that the paddle starts on screen; notice the PLUS

# Ball
# ball = name; turtle = module name; Turtle = class name
ball = turtle.Turtle()
ball.speed(0)  #speed of animation to max possible speed
ball.shape("square")
ball.color("white")
ball.penup() #draw a line
ball.goto(0, 0)  #this is the location that the paddle starts on screen
ball.dx = .4 #dy and dy is the movement by two pixels
ball.dy = .4

# pen - scoreboard
pen  = turtle.Turtle()
pen.speed(0) #animation speed, not movement
pen.color("white")
pen.penup() #we don't want to draw a line when the pen moves
pen.hideturtle() #we don't want to see it on the screen, just the text
pen.goto(0, 260)
pen.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, "normal"))

#function (piece of a program that something has already been defined)
def paddle_a_up():
    y = paddle_a.ycor() #on the y coordinate
    y += 20 #add 20 pixels to y coordinates
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor() #on the y coordinate
    y -= 20 #subtracts 20 pixels to y coordinates
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor() #on the y coordinate
    y += 20 #add 20 pixels to y coordinates
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor() #on the y coordinate
    y -= 20 #subtracts 20 pixels to y coordinates
    paddle_b.sety(y)

# keyboard binding
wn.listen() #tells it to listen to keyboard input
wn.onkeypress(paddle_a_up, "w") #when the user presses w, call the function paddle_a_up
wn.onkeypress(paddle_a_down, "s") #when user presses s, call the function paddle_a_down
wn.onkeypress(paddle_b_up, "Up") #Up and Down capitalized are the arrow keys
wn.onkeypress(paddle_b_down, "Down")

# Main game loop
while True:
    wn.update()

    # move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # border checking
    if ball.ycor() > 290:
            ball.sety(290)
            ball.dy *= -1 #reverses the direction of the ball

    if ball.ycor() < -290:
            ball.sety(-290)
            ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0, 0) #ball is sent back to center
        ball.dx *= -1
        score_a += 1 #adds a point for player A
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1 #adds a point for player B
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

    # paddle and ball collisions
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() -40):
        ball.setx(340)
        ball.dx *= -1

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() -40):
        ball.setx(-340)
        ball.dx *= -1
