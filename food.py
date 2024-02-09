from turtle import Turtle
from random import randint


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(0.5)
        self.color("green")
        self.speed("fastest")
        self.penup()
        self.position_food()

    def position_food(self):
        """
        Position food on the screen
        :return: None
        """
        x = randint(-270, 270)
        y = randint(-270, 270)
        self.goto(x, y)
