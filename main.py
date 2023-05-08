from turtle import Turtle, Screen
import time
from car import Car
import random
from scoreboard import Score
from frogger import Frogger

cars = []

screen = Screen()
screen.setup(600, 600)
screen.tracer(0)
screen.colormode(255)
screen.listen()


score = Score()
frogger = Frogger()

screen.onkey(frogger.move, "Up")


def create_car():
    if bool(random.getrandbits(1)):
        car = Car()
        cars.append(car)


game_is_on = True
counter = 0
while game_is_on:
    screen.update()
    time.sleep(0.05)
    counter += 1
    if counter == 10:
        create_car()
        counter = 0
    for c in cars:
        if c.xcor() > -330:
            c.move_car()
        else:
            cars.remove(c)
            c.hideturtle()

screen.exitonclick()

