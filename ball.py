from turtle import Turtle
import random


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shapesize(1)
        self.penup()
        self.color('blue')
        self.shape('circle')
        self.speed(7)
        self.setheading(random.randrange(-50, 50))
        self.ball_on_the_run()
        self.ball_speed = 0.1

    def ball_on_the_run(self):
        self.forward(10)

    def p1_score_set(self):
        self.home()
        self.setheading(random.randrange(140, 240))
        self.ball_speed *= 0.85

    def p2_score_set(self):
        self.home()
        self.setheading(random.randrange(-50, 50))
        self.ball_speed *= 0.85
