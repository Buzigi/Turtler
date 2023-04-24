import random, threading, time
from turtle import Turtle
class Car(Turtle):

    def __init__(self):
        super().__init__()
        self.color((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
        self.shape("square")
        self.penup()
        y_pos = random.randint(-200, 200)
        length = (1+random.random()) * 1
        height = (1+random.random()) * 2
        self.shapesize(stretch_wid= length, stretch_len= height)
        self.goto(300, y_pos)
        self.speed_ratio = random.randint(1, 5)
        self.counter = 1

    def move_car(self):
        if self.counter % self.speed_ratio == 0:
            self.goto(self.xcor() - 10, self.ycor())
        self.counter += 1
