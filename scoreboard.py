from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.hideturtle()
        self.goto(-200,170)
        self.update_level()

    def update_level(self):
        self.clear()
        self.write(f"Level: {self.level}", align="center", font=("Arial", 15, "normal"))

    def game_over(self):
        self.goto(0,0)
        self.write(f"Game Over", align="center", font=("Arial", 15, "normal"))