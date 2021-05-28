import turtle

class Ball():

    dx = 0.15
    dy = 0.15

    def __init__(self):
        self.placar_bola = Placar()

        self.ball = turtle.Turtle()
        self.ball.speed(0)  # speed of animation
        self.ball.shape("circle")
        self.ball.color("white")
        self.ball.penup()
        self.ball.goto(0, 0)

        self.ball.dx = 0.15
        self.ball.dy = 0.15

    def move(self, dx, dy):

        self.ball.setx(self.ball.xcor() + self.dx)
        self.ball.sety(self.ball.ycor() + self.dy)

        #top border
        if self.ball.ycor() > 290:
            self.ball.sety(290)
            self.dy *= -1

        # bottom border
        if self.ball.ycor() < -290:
            self.ball.sety(-290)
            self.dy *= -1

         #left border
        if self.ball.xcor() > 390:
            self.ball.setx(390)
            self.ball.goto(0, 0)
            self.dx *= -1
            self.placar_bola.score_a += 1
            self.placar_bola.pen.clear()
            self.placar_bola.pen.write(f"Player A: {self.placar_bola.score_a}    Player B: {self.placar_bola.score_b}", align="center", font=("Courier", 24, "normal") )


        #right border
        if self.ball.xcor() < -390:
            self.ball.setx(-390)
            self.ball.goto(0,0)
            self.dx *= -1
            self.placar_bola.score_b += 1
            self.placar_bola.pen.clear()
            self.placar_bola.pen.write(f"Player A: {self.placar_bola.score_a}    Player B: {self.placar_bola.score_b}", align="center", font=("Courier", 24, "normal") )


class Paddles():
    def __init__(self):

        self.bola_act = Ball()

        self.paddle_a = turtle.Turtle()
        self.paddle_a.speed(0)  # speed of animation
        self.paddle_a.shape("square")
        self.paddle_a.shapesize(stretch_wid=5, stretch_len=1)
        self.paddle_a.color("white" )
        self.paddle_a.penup()
        self.paddle_a.goto(-350, 0)

        self.paddle_b = turtle.Turtle ()
        self.paddle_b.speed ( 0 )  # speed of animation
        self.paddle_b.shape ( "square" )
        self.paddle_b.shapesize ( stretch_wid=5, stretch_len=1 )
        self.paddle_b.color ( "white" )
        self.paddle_b.penup ()
        self.paddle_b.goto ( 350, 0 )

    def paddle_a_up(self):
        y_a_up = self.paddle_a.ycor() #coordenada y
        y_a_up += 20
        self.paddle_a.sety(y_a_up)

    def paddle_a_down(self):
        y_a_down = self.paddle_a.ycor() #coordenada y
        y_a_down -= 20
        self.paddle_a.sety(y_a_down)

    def paddle_b_up(self):
        y_b_up = self.paddle_b.ycor() #coordenada y
        y_b_up += 20
        self.paddle_b.sety(y_b_up)

    def paddle_b_down(self):
        y_b_down = self.paddle_b.ycor() #coordenada y
        y_b_down -= 20
        self.paddle_b.sety(y_b_down)


    def colisao(self):
        # paddle collisions
        if (self.bola_act.xcor () > 340 and self.bola_act.xcor () < 350) and (
                self.bola_act.ycor () < self.paddle_b.ycor () + 40 and self.bola_act.ycor () > self.paddle_b.ycor () - 40) :
            self.bola_act.setx ( 340 )
            self.dx *= -1

        if (self.bola_act.xcor () < -340 and self.bola_act.xcor () > -350) and (
                self.bola_act.ycor () < self.paddle_a.ycor () + 40 and self.bola_act.ycor () > self.paddle_a.ycor () - 40) :
            self.bola_act.setx ( -340 )
            self.dx *= -1


class Placar():
    def __init__(self):
        self.score_a = 0
        self.score_b = 0

        self.pen = turtle.Turtle()
        self.pen.speed(0)
        self.pen.color("white")
        self.pen.penup()
        self.pen.hideturtle()
        self.pen.goto(0, 260)
        # self.pen.write(f"Player A: {self.score_a}    Player B: {self.score_b}", align="center", font=("Courier", 24, "normal"))


class Board():
    def __init__(self): #p1, p2, placar
        self.bola = Ball()
        self.raquetes = Paddles()
        self.placar = Placar()

        self.wn = turtle.Screen()
        self.wn.title("Pong @ FIAP")
        self.wn.bgcolor("black")
        self.wn.setup(width=800, height=600)
        self.wn.tracer(0)

    def keyboard(self):
        self.wn.listen()
        self.wn.onkeypress(self.raquetes.paddle_a_up, 'w')
        self.wn.onkeypress(self.raquetes.paddle_a_down, 's')
        self.wn.onkeypress(self.raquetes.paddle_b_up, 'Up')
        self.wn.onkeypress(self.raquetes.paddle_b_down, 'Down')

    def play(self):
        while True:
            self.wn.update()
            self.bola.move(0.15, 0.15)
            self.keyboard()

if __name__ == '__main__':
    game = Board()
    game.play()

