from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
  cars = []
  def __init__(self):
    super().__init__()
    self.hideturtle()
    self.create_cars()
    self.movement_speed = STARTING_MOVE_DISTANCE
    
  def create_cars(self):
    for _ in range(22):
      car = Turtle()
      car.penup()
      car.shape("square")
      car.shapesize(stretch_len=2, stretch_wid=1)
      car.color(random.choice(COLORS))
      car.goto(self.random_position())
      self.cars.append(car)
    
  def hits_left_wall(self):
    if self.xcor() < -280:
      print('hi')
        
  def refresh(self, car):
    car.goto(300, random.randint(-220, 250))
    
  def move(self):
    for car in self.cars:
      car.goto(car.xcor()-self.movement_speed, car.ycor())
      if car.xcor() < -320:
        self.refresh(car)
    
  def random_position(self):
    return (random.randint(-280, 280), random.randint(-220,250))
  
  def speed_up(self):
    self.movement_speed += MOVE_INCREMENT
      
  