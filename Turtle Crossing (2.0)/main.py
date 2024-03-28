import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle Crossing")
screen.tracer(0)

level = 1
player = Player()
scoreboard = Scoreboard()

cars = []
timer = 0

screen.listen()
screen.onkey(player.go_up, "Up")
screen.onkey(player.go_down, "Down")
screen.onkey(player.go_left, "Left")
screen.onkey(player.go_right, "Right")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    timer += 1
    if timer >= 10:
        car = CarManager()
        cars.append(car)
        timer = 0
    for car in cars:
        car.move(level=scoreboard.level)
        if car.distance(player) < 17:
            game_is_on = False
            scoreboard.game_over()
    if scoreboard.level >= 5:
        more_cars = CarManager()
        cars.append(more_cars)
    if player.ycor() >= 280:
        player.level_reset()
        scoreboard.increase_level()

screen.exitonclick()
