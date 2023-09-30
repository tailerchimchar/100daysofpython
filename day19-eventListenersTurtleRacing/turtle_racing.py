from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500,height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtles = []

for index in range(1,7):
  turtle_object = Turtle(shape="turtle")
  turtle_object.color(colors[index-1])
  turtle_object.penup()
  turtle_object.goto(-225, 200 - (50 * index))
  all_turtles.append(turtle_object)

#tim = Turtle(shape="turtle", color="red")
#tim.goto(x=230, y=100)

if user_bet:
  is_race_on =  True

while is_race_on:
  for turtle in all_turtles:
    if turtle.xcor() > 250:
      is_race_on = False
      winning_color = turtle.pencolor()
      if winning_color == user_bet:
        print(f"You've won! The {winning_color} turtle is the winner!")
      else:
        print(f"You've lost! The {winning_color} turtle is the winner!")
    rand_distance = random.randint(0,10)
    turtle.forward(rand_distance)
    
screen.exitonclick()
