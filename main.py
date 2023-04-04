import random
from turtle import Screen
from display import DisplaySet
from paddle import Paddle
from ball import Ball
from score import Score
import time

screen = Screen()
screen.title('PONG')
screen.bgcolor('black')
screen.setup(height=600, width=800)
screen.tracer(0)
set_game_field = DisplaySet()
game_on = True
ball = Ball()
score = Score()
score_p1 = Score()
score_p2 = Score()
paddle_1 = Paddle()
paddle_2 = Paddle()

paddle_1.paddle_position(-350)
score_p1.score_position(-120)
paddle_2.paddle_position(350)
score_p2.score_position(100)

screen.listen()
screen.onkey(paddle_1.paddle_up, 'q')
screen.onkey(paddle_1.paddle_down, 'a')

screen.onkey(paddle_2.paddle_up, 'Up')
screen.onkey(paddle_2.paddle_down, 'Down')

while game_on:
    time.sleep(ball.ball_speed)
    screen.update()
    ball.ball_on_the_run()
    tilt_angle = random.randrange(4, 8)
    if ball.ycor() > 280 or ball.ycor() < -280:
        new_angle = 360 - ball.heading()
        ball.setheading(new_angle)

    elif ball.distance(paddle_1) < 50 and ball.xcor() < -330:
        new_angle = 360 - (ball.heading() * 2 - tilt_angle)
        ball.setheading(new_angle)

    elif ball.distance(paddle_2) < 50 and ball.xcor() > 330:
        new_angle = 180 - (ball.heading() * 2 + tilt_angle)
        ball.setheading(new_angle)

    elif ball.xcor() > 370:
        ball.p1_score_set()
        score_p1.score_count()

    elif ball.xcor() < -370:
        ball.p2_score_set()
        score_p2.score_count()

    if score_p1.score == 10 or score_p2.score == 10:
        score.end_game()
        game_on = False

screen.exitonclick()
