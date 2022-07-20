import time
from turtle import Turtle
ALIGNMENT = "center"
FONT = ("verdana", 10, "bold")

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.goto(0, 280)
        self.score = 0
        with open("data.txt") as data:
            self.high_score = int(data.read())

    def update_score(self):
        self.clear()
        self.write(arg=f"Score: {self.score}  Highscore : {self.high_score}", align=ALIGNMENT, font=FONT)

    def game_start_over(self):
        self.goto(0, 0)
        self.write(arg="GAME OVER!", align=ALIGNMENT, font=FONT)
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.high_score}")
        time.sleep(2)
        self.clear()
        self.goto(0, 280)
        self.score = 0
        self.update_score()





