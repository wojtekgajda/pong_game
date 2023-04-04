from turtle import Turtle

PADDLE_STEP = 40


class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.resizemode('user')
        self.color('white')
        self.shape('square')
        self.shapesize(5, 1, 1)
        self.penup()
        self.speed('fastest')
        self.y = 0

    def paddle_position(self, x_cor):
        self.goto(x_cor, 0)

    def paddle_up(self):
        y = self.ycor() + PADDLE_STEP
        self.sety(y)

    def paddle_down(self, ):

        y = self.ycor() - PADDLE_STEP
        self.sety(y)
