
from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.set_food()

    def set_food(self):
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.color("pink")
        self.speed(0)
        self.random_position()

    def random_position(self):
        x_cor = random.randint(-280, 280)
        y_cor = random.randint(-280, 280)
        self.goto(x_cor, y_cor)

    def reset_food(self):
        self.clear()
        self.set_food()


