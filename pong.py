import turtle

window = turtle.Screen()
window.title("PONG GAME")
window.bgcolor("black")
window.setup(width=800, height=600)
window.tracer(0)

#score
score_a = 0
score_b = 0

#paddleA
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.shapesize(stretch_wid=4, stretch_len=0.5)
paddle_a.color("white")
paddle_a.penup()
paddle_a.goto(-370,0)

#paddleB
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.shapesize(stretch_wid=4, stretch_len=0.5)
paddle_b.color("white")
paddle_b.penup()
paddle_b.goto(370,0)

#ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.dx = 0.8
ball.dy = -0.8

#pen
pen = turtle.Turtle()
pen.color("white")
pen.speed(0)
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player A: 0  Player B: 0", align="center", font=("courier",20, "normal"))

#border line
line = turtle.Turtle()
line.speed(0)
line.color("white")
line.shape("square")
line.penup()
line.shapesize(stretch_len=40, stretch_wid=0.1)
line.goto(-0,250)

#Function
def paddle_a_up():
    y = paddle_a.ycor()
    y += 35
    paddle_a.sety(y)


def paddle_a_down():
    y = paddle_a.ycor()
    y -= 35
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    y += 35
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 35
    paddle_b.sety(y)

window.listen()
window.onkeypress(paddle_a_up, "w")
window.onkeypress(paddle_a_down, "s")
window.onkeypress(paddle_b_up, "Up")
window.onkeypress(paddle_b_down, "Down")


#main game loop
while True:
    window.update()

    #ball border checking
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    if ball.ycor() > 240:
        ball.sety(240)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0,0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("courier", 20, "normal"))

    if ball.xcor() < -390:
        ball.goto(0,0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("courier", 20, "normal"))

    if (ball.xcor() > 350 and ball.xcor() < 360) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() -40):
        ball.setx(350)
        ball.dx *= -1

    if (ball.xcor() < -350 and ball.xcor() > -360) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() -40):
        ball.setx(-350)
        ball.dx *= -1

    #paddle border
    if paddle_a.ycor() > 210:
        paddle_a.sety(210)

    if paddle_a.ycor() < -240:
        paddle_a.sety(-240)

    if paddle_b.ycor() > 210:
        paddle_b.sety(210)

    if paddle_b.ycor() < -240:
        paddle_b.sety(-240)


