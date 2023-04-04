from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.score = 0
        self.hideturtle()
        self.color('white')

    def score_count(self):
        self.score += 1
        self.clear()
        self.write(f'{self.score}', align='center', font=('Roboto', 44, 'normal'))

    def score_position(self, x_cor):
        self.goto(x_cor, 240)
        self.write(f'{self.score}', align='center', font=('Roboto', 44, 'normal'))

    def end_game(self):
        self.goto(0, 0)
        self.write(f'GAME OVER', align='center', font=('Roboto', 44, 'normal'))
