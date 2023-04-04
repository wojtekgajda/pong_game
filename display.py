from turtle import Turtle, Screen


class DisplaySet(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.pensize(5)
        self.pencolor('white')
        self.shape('square')
        self.draw_middle_line()
        self.draw_pitch()

    def draw_middle_line(self):
        self.goto(-10, -400)
        self.setheading(90)
        for i in range(-390, 390, 20):
            self.pendown()
            self.forward(20)
            self.penup()
            self.forward(20)

    def draw_pitch(self):
        self.pencolor('green')
        self.goto(-400, 300)
        self.pendown()
        self.setheading(0)
        self.forward(800)
        self.penup()

        self.goto(-400, -290)
        self.pendown()
        self.setheading(0)
        self.forward(800)
