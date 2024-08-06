from turtle import Screen
from car import Car
from player import Player
from scoreboard import Scoreboard
import time

# setup screen
screen = Screen()
screen.setup(500,400)
screen.bgcolor("white")
screen.tracer(0)

# create object
car = Car()
player = Player()
scoreboard = Scoreboard()

# call function when keypress
screen.listen()
screen.onkeypress(key="Up", fun=player.func_up)

# game start
game_on = True

while game_on:
    time.sleep(car.speed_car)
    screen.update()

    car.create_car()
    car.move()

    # when player cross the road completely
    if player.ycor() > 200:
        car.speed_car *= 0.7
        scoreboard.level += 1
        scoreboard.update_level()
        player.reset_position()

    # collision with car
    if car.detect_collision(player):
        game_on = False
        scoreboard.game_over()

screen.exitonclick()