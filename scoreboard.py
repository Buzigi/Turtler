from turtle import Turtle


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.level = 1
        self.hideturtle()
        self.color("black")
        self.write_score()

    def write_score(self):
        self.goto(0, 240)
        self.write(f"Level: {self.level}", align="center", font=("Courier", 40, "normal"))
