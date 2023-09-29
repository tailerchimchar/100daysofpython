from turtle import Turtle, Screen
import random 

# Draw a triangle, square, pentagon, hexagon, heptagon, octagon, nonagon, and decagon 
timmy = Turtle()
timmy.shape("turtle")
timmy.color("red")

colors = ["Blue", "red", "green", "deepskyblue", "lightseagreen", "wheat", "black", "orange"]

num_sides = 3
while num_sides != 10:
  timmy.color(random.choice(colors))
  for _ in range(num_sides):
    angle = 360
    timmy.forward(100)
    timmy.right(angle / num_sides)
  num_sides+=1

screen = Screen()
screen.exitonclick()