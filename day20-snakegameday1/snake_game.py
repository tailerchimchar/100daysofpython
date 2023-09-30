from turtle import Screen, Turtle

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
all_snakes = []

for i in range(3):
  snake_object = Turtle(shape="square")
  snake_object.color("white")
  #snake_object.shapesize(20,20,0)
  all_snakes.append(snake_object)
  snake_object.goto(snake_object.xcor() + 20*i,0)


screen.exitonclick()