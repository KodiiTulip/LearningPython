# Simple Pong game
import winsound
import turtle

# special variables
scH = 600
scW = 800

# window root and a simple title
wn = turtle.Screen()
wn.title("Pong by KodiiTulip")
# window's background color
wn.bgcolor("black")
# setting up the window's size
wn.setup(width=scW, height=scH)
# stop the window from updating
wn.tracer(0)

# adding the paddles
# paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-(wn.window_width() / 2) + (wn.window_width() / 18), 0)

# paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto((wn.window_width() / 2) - (wn.window_width() / 18), 0)

# ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 1
ball.dy = 1

# scores
scoreA = 0
scoreB = 0

# pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, (wn.window_height()/2) - (wn.window_height()/18))
pen.write(f"Player A: {scoreA}  Player B: {scoreB}", align="center", font=("Courier", 24, "bold"))


# functions
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)


def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)


def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)


def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)


def bpdB_yCol():
    if paddle_b.xcor() > ball.xcor() > paddle_b.xcor()-10 and paddle_b.ycor()+40 > ball.ycor() > paddle_b.ycor()-50:
        return True
    else:
        return False


def bpdA_yCol():
    if paddle_a.xcor() < ball.xcor() < paddle_a.xcor()+10 and paddle_a.ycor()+40 > ball.ycor() > paddle_a.ycor()-50:
        return True
    else:
        return False


# keyboard bind
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")

# main game loop
while True:
    wn.update()

    # moving ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # border check
    if ball.ycor() > (wn.window_height() / 2) - 10:
        ball.sety((wn.window_height() / 2) - 10)
        winsound.PlaySound('sounds\\bounce', winsound.SND_ASYNC)
        ball.dy *= -1
    elif ball.ycor() < -(wn.window_height() / 2) + 10:
        ball.sety(-(wn.window_height() / 2) + 10)
        winsound.PlaySound('sounds\\bounce', winsound.SND_ASYNC)
        ball.dy *= -1
    elif ball.xcor() > (wn.window_width() / 2) - 10:
        ball.goto(0, 0)
        ball.dx *= -1
        scoreA += 1
        pen.clear()
        pen.write(f"Player A: {scoreA}  Player B: {scoreB}", align="center", font=("Courier", 24, "bold"))
    elif ball.xcor() < -(wn.window_width() / 2) + 10:
        ball.goto(0, 0)
        ball.dx *= -1
        scoreB += 1
        pen.clear()
        pen.write(f"Player A: {scoreA}  Player B: {scoreB}", align="center", font=("Courier", 24, "bold"))

    # addapting paddles xcor
    paddle_a.setx(-(wn.window_width() / 2) + (wn.window_width() / 16))
    paddle_b.setx((wn.window_width() / 2) - (wn.window_width() / 16))

    # addapting pen ycor
    pen.sety((wn.window_height()/2) - (wn.window_height()/18))

    # paddle ball collision
    if bpdB_yCol() or bpdA_yCol():
        winsound.PlaySound('sounds\\bounce', winsound.SND_ASYNC)
        ball.dx *= -1
