from turtle import Screen, Turtle
import time
from paddel import Paddel
from ball import Ball
from scoreboard import Scorboard

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")

screen.tracer(0)

scoreboard = Scorboard()

paddel_dx = Paddel(375)
paddel_sx = Paddel(-375)

#paddel sx moving up when press key "up" and down when press key "down"
screen.listen()
screen.onkey(key="Up", fun=paddel_dx.up)
screen.onkey(key="Down", fun=paddel_dx.down)

#paddel sx moving up when press key "w" and down when press key "s"
screen.onkey(key="w", fun=paddel_sx.up)
screen.onkey(key="s", fun=paddel_sx.down)

ball = Ball()


game_on = True

while game_on:
    time.sleep(ball.speed_move)
    ball.move()

    #detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    #detect collision with paddel
    if ball.distance(paddel_dx) < 30 and ball.xcor() > 320 or ball.distance(paddel_sx) < 30 and ball.xcor() < -320:
        ball.bounce_x()

    #detect missing collision with rx_paddel

    if ball.xcor() > 420:
        ball.reset_position()
        scoreboard.score_sx()

    #detect missis sx_paddel

    if ball.xcor() < -420:
        ball.reset_position()
        scoreboard.score_dx()

    screen.update()




screen.exitonclick()