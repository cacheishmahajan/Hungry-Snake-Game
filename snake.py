from turtle import Turtle, Screen
import time

screen = Screen()
XCOORD = [0, -20, -40]
MOVE_DISTANCE = 20


class Snake:
    def __init__(self):
        self.turtles = []
        self.create_snake()

    def create_snake(self):
        for num in range(3):
            new_turtle = Turtle(shape="square")
            new_turtle.speed(1)
            new_turtle.penup()
            new_turtle.color("white")
            new_turtle.goto(XCOORD[num], 0)
            self.turtles.append(new_turtle)

    def up(self):
        if self.turtles[0].heading() == 270:
            pass
        else:
            self.turtles[0].setheading(90)

    def down(self):
        if self.turtles[0].heading() == 90:
            pass
        else:
            self.turtles[0].setheading(270)

    def right(self):
        if self.turtles[0].heading() == 180:
            pass
        else:
            self.turtles[0].setheading(0)

    def left(self):
        if self.turtles[0].heading() == 0:
            pass
        else:
            self.turtles[0].setheading(180)

    def move(self):
        for num in range(len(self.turtles) - 1, -1, -1):
            if num != 0:
                self.turtles[num].goto(self.turtles[num - 1].position())
            else:
                self.turtles[0].forward(MOVE_DISTANCE)

    def extend_snake(self):
        new_turtle = Turtle(shape="square")
        new_turtle.speed(1)
        new_turtle.penup()
        new_turtle.color("white")
        new_turtle.goto(self.turtles[-1].position())
        self.turtles.append(new_turtle)

    def reset_snake(self):
        for h in self.turtles:
            h.goto(600, 600)
        self.turtles.clear()
        self.create_snake()
