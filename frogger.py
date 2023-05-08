from turtle import Turtle


class Frogger(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(0, -250)
        self.color("green")
        self.shape("turtle")
        self.shapesize(stretch_wid=2, stretch_len=2)
        self.setheading(90)

    def move(self):
        self.goto(self.xcor(), self.ycor() + 10)
