import turtle 

wn = turtle.Screen()

wn.title ("Pong")
wn.bgcolor ("black")
wn.setup (width = 800, height = 600)
wn.tracer (0)

#scoring system

scoreA = 0
scoreB = 0


#Pong A

paddle_a = turtle.Turtle ()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color ("red")
paddle_a.shapesize (stretch_wid = 5, stretch_len = 1)
paddle_a.penup ()
paddle_a.goto(-350, 0)


#Pong B
paddle_b = turtle.Turtle ()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color ("blue")
paddle_b.shapesize (stretch_wid = 5, stretch_len = 1)
paddle_b.penup ()
paddle_b.goto(350, 0)

#ball 
ball = turtle.Turtle()
ball.speed (0)
ball.shape ("square")
ball.color ("white")
ball.penup()
ball.goto(0,0)
ball.dx = 0.15
ball.dy = -0.15

#pen

pen = turtle.Turtle ()
pen.speed (0)
pen.color ("white")
pen.penup()
pen.hideturtle ()
pen.goto (0,260)
pen.write ("Player 1: 0   Player 2: 0", align = "center", font= ("courier", 24, "normal"))

def paddleA_up ():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)

def paddleA_down ():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)


def paddleB_up ():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)

def paddleB_down ():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)

#keyboard binding
wn.listen ()
wn.onkeypress(paddleA_up, "w")
wn.onkeypress(paddleA_down, "s")

wn.onkeypress(paddleB_up, "Up")
wn.onkeypress(paddleB_down, "Down")

while True:
    wn.update()

    #Ball movement
    ball.setx(ball.xcor () + ball.dx)
    ball.sety (ball.ycor() + ball.dy)

    #border
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
    
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        scoreA += 1
        pen.clear ()
        pen.write ("Player 1: {}    Player 2: {}".format (scoreA, scoreB), align = "center", font= ("courier", 24, "normal"))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        scoreB += 1
        pen.clear()
        pen.write ("Player 1: {}    Player 2: {}".format (scoreA, scoreB), align = "center", font= ("courier", 24, "normal"))

    #paddle ball hit

    if ball.xcor () > 340 and ball.xcor () < 350 and (ball.ycor() < paddle_b.ycor() +40 and ball.ycor() > paddle_b.ycor() -40):
        ball.setx(340)
        ball.dx *= -1

    if ball.xcor () < -340 and ball.xcor () > -350 and (ball.ycor() < paddle_a.ycor() +40 and ball.ycor() > paddle_a.ycor() -40):
        ball.setx(-340)
        ball.dx *= -1