from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Arcade Game")
screen.tracer(0)

fire = ("🔥", '#FF4500')
r_paddle = Paddle((360, 0),fire[1])

water = ("💧", '#00BFFF')
l_paddle = Paddle((-360, 0),water[1])

ball = Ball()
scoreboard = Scoreboard(fire, water)
game_is_on = True

screen.listen()
screen.onkey(l_paddle.go_up, "q")
screen.onkey(l_paddle.go_down, "a")
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # ball bouncing logic
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # detect collision of ball with paddle
    if (ball.distance(r_paddle) < 30 and ball.xcor() > 290) or (ball.distance(l_paddle) < 30 and ball.xcor() < -290):
        ball.bounce_x()

    # detect R paddle miss
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    # detect L paddle miss
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()

    # game over if either l paddle or right paddle first scores 10 points
    if scoreboard.l_score >= 10 or scoreboard.r_score >= 10:
        scoreboard.game_over()
        game_is_on = False

screen.exitonclick()