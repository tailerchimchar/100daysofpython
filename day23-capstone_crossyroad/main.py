import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

player = Player()
screen.onkey(player.move_up, 'w')
screen.onkey(player.move_left, 'a')
screen.onkey(player.move_right, 'd')
screen.onkey(player.move_down, 's')

cars = CarManager()
scoreboard = Scoreboard()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    cars.move()
    
    # detect collision with car
    for car in cars.cars:
      if player.distance(car) < 20:
        scoreboard.game_over()
        game_is_on = False
      
    # detect turtle crosses 280
    if player.is_at_finish():
      scoreboard.level_up()
      cars.speed_up()
      player.refresh()
      
screen.exitonclick()
    
