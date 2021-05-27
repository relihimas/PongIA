import turtle

# 1) Implantar classes e funçoes


#janela do jogo
wn = turtle.Screen()
wn.title("Pong @ FIAP")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

#score

score_a = 0
score_b = 0

# Paddle A

paddle_a = turtle.Turtle()
paddle_a.speed(0)    #speed of animation
paddle_a.shape("square")
paddle_a.shapesize(stretch_wid=5,stretch_len=1)
paddle_a.color("white")
paddle_a.penup()
paddle_a.goto(-350,0)

# Paddle B

paddle_b = turtle.Turtle()
paddle_b.speed(0)    #speed of animation
paddle_b.shape("square")
paddle_b.shapesize(stretch_wid=5,stretch_len=1)
paddle_b.color("white")
paddle_b.penup()
paddle_b.goto(350,0)

# Ball

ball = turtle.Turtle()
ball.speed(0)    #speed of animation
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0,0)

ball.dx = 0.15
ball.dy = 0.15

#Pen

pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write(f"Player A: {score_a}    Player B: {score_b}", align="center", font=("Courier", 24, "normal"))

#move the paddles - Functions

def paddle_a_up():
    y_a_up = paddle_a.ycor() #coordenada y
    y_a_up += 20
    paddle_a.sety(y_a_up)

def paddle_a_down():
    y_a_down = paddle_a.ycor() #coordenada y
    y_a_down -= 20
    paddle_a.sety(y_a_down)

def paddle_b_up():
    y_b_up = paddle_b.ycor() #coordenada y
    y_b_up += 20
    paddle_b.sety(y_b_up)

def paddle_b_down():
    y_b_down = paddle_b.ycor() #coordenada y
    y_b_down -= 20
    paddle_b.sety(y_b_down)


#keyobard binding

wn.listen()
wn.onkeypress(paddle_a_up, 'w')
wn.onkeypress(paddle_a_down, 's')
wn.onkeypress(paddle_b_up, 'Up')
wn.onkeypress(paddle_b_down, 'Down')


# Main game loop
while True:
    wn.update()
    #move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #border checking
    #top border
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
    # bottom border
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    #left border
    if ball.xcor() > 390:
        ball.setx(390)
        ball.goto(0,0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write(f"Player A: {score_a}    Player B: {score_b}", align="center", font=("Courier", 24, "normal") )

    #right border
    if ball.xcor() < -390:
        ball.setx(-390)
        ball.goto(0,0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write(f"Player A: {score_a}    Player B: {score_b}", align="center", font=("Courier", 24, "normal") )

    #paddle collisions
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() -40):
        ball.setx(340)
        ball.dx *= -1

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() -40):
        ball.setx(-340)
        ball.dx *= -1
