from turtle import Turtle

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.goto(0,-180)
        self.setheading(90)

    def func_up(self):
        self.forward(10)

    def reset_position(self):
        self.goto(0,-180)