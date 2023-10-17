from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time

START_POSITION = [(350, 0), (-350, 0)]

screen = Screen()
screen.setup(width=800, height=600)
screen.bgpic("images/pong_bg.gif")
screen.title("PONG Game")
screen.tracer(0)

right_paddle = Paddle(START_POSITION[0])
left_paddle = Paddle(START_POSITION[1])
ball = Ball()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(right_paddle.move_up, "Up")
screen.onkey(right_paddle.move_down, "Down")
screen.onkey(left_paddle.move_up, "w")
screen.onkey(left_paddle.move_down, "s")

game_on = True
while game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
# Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
# Detect collision with paddle
    if ball.distance(right_paddle) < 50 and ball.xcor() > 320 or ball.distance(left_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
# Detect paddle miss
    if ball.xcor() > 380:
        ball.reset_ball()
        scoreboard.left_point()
        time.sleep(0.5)
    if ball.xcor() < -380:
        ball.reset_ball()
        scoreboard.right_point()
        time.sleep(0.5)
    if scoreboard.left_score == 3 or scoreboard.right_score == 3:
        game_on = False
        scoreboard.game_over()

screen.exitonclick()
