
from turtle import Turtle
import random

class Car(Turtle):
    def __init__(self):
        self.speed_car = 0.1
        self.all_car = []

    def create_car(self):
        chance = random.randint(1,6)
        if chance == 1:
            new_car = Turtle("square")
            new_car.penup()
            new_car.goto(250,random.randint(-130,180))
            new_car.shapesize(stretch_len=1, stretch_wid=0.5)
            new_car.color(self.random_color())
            self.all_car.append(new_car)

    def random_color(self):
        r = random.random()
        g = random.random()
        b = random.random()

        return (r,g,b)
    
    def move(self):
        for i in self.all_car :
            i.backward(5)

    def detect_collision(self, player):
        for car in self.all_car:
            if car.distance(player) < 15:
                return True
        return False