from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()
screen.listen()

def move_forwards():
  tim.fd(15)

def move_backwards():
  tim.backward(15)

def turn_left():
  tim.left(5)

def turn_right():
  tim.right(5)

def clear_screen():
  screen.clearscreen()

screen.onkeypress(key = "w", fun = move_forwards)
screen.onkeypress(key = "a", fun = turn_left)
screen.onkeypress(key = "s", fun = move_backwards)
screen.onkeypress(key = "d", fun = turn_right)
screen.onkeypress(key = "c", fun = clear_screen)


screen.exitonclick()