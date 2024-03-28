from turtle import Turtle
from random import choice, randint

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
MOVE_INCREMENT = 10
SHAPE = "square"


class CarManager(Turtle):

    def __init__(self):
        super().__init__()
        self.shape(SHAPE)
        self.color(choice(COLORS))
        self.shapesize(stretch_wid=1, stretch_len=3)
        self.shapesize()
        self.penup()
        self.random_y = randint(-250, 250)
        self.goto(300, self.random_y)
        self.setheading(180)

    def move(self, level):
        self.forward(MOVE_INCREMENT * level)

    def again(self):
        self.random_y = randint(-250, 250)
        self.goto(300, self.random_y)
