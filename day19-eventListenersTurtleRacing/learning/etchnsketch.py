from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()
screen.listen()

def move_forwards():
  tim.fd(10)

def move_backwards():
  tim.backward(10)

def turn_left():
  tim.left(10)

def turn_right():
  tim.right(10)

def clear_screen():
  screen.clearscreen()
  tim.penup()
  tim.home()
  tim.pendown()
  tim.showturtle()

screen.onkeypress(key = "w", fun = move_forwards)
screen.onkeypress(key = "a", fun = turn_left)
screen.onkeypress(key = "s", fun = move_backwards)
screen.onkeypress(key = "d", fun = turn_right)
screen.onkeypress(key = "c", fun = clear_screen)


screen.exitonclick()