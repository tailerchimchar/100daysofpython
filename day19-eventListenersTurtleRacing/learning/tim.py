from turtle import Turtle, Screen
tim = Turtle()
screen = Screen()
screen.listen()

def move_forwards():
  tim.fd(10)
screen.onkey(key = "space", fun = move_forwards)
screen.exitonclick()