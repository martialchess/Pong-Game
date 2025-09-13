from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard, Divider

WINNING_SCORE = 10

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("PONG")
screen.tracer(0)

left_paddle = Paddle((-380, 0))
right_paddle = Paddle((380, 0))
ball = Ball()
divider = Divider()

#Scoreboards
left_score = Scoreboard(position=(-200, 260))
right_score = Scoreboard(position=(200, 260))

screen.listen()
screen.onkeypress(left_paddle.up, "w")
screen.onkeypress(left_paddle.down, "s")
screen.onkeypress(right_paddle.up, "Up")
screen.onkeypress(right_paddle.down, "Down")
# screen.onkeypress(ball.move, "")

# Main Game Loop

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()

    # Detect collision with top and bottom walls
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Paddle bounce
    if (ball.distance(right_paddle) < 50 and ball.xcor() > 320) or \
       (ball.distance(left_paddle) < 50 and ball.xcor() < -320):
        ball.bounce_x()

    # Detect if ball goes past right wall
    if ball.xcor() > 380:
        ball.reset_position()
        left_score.increase_score()
        # increase left player’s score here

    # Detect if ball goes past left wall
    if ball.xcor() < -380:
        ball.reset_position()
        right_score.increase_score()
        # increase right player’s score here

    # Winning Condition
    if left_score.score >= WINNING_SCORE:
        left_score.game_over("Left Player")
        game_is_on = False
    elif right_score.score >= WINNING_SCORE:
        right_score.game_over("Right Player")
        game_is_on = False



screen.exitonclick()