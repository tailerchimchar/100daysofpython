from turtle import Turtle, Screen

#makes object
timmy = Turtle()

print(timmy)

my_screen = Screen()
timmy.shape("turtle")
timmy.color("green")
timmy.forward(100)
my_screen.exitonclick()