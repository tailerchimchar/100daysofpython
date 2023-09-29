import turtle as t
import random 

def random_color():
  return (random.randint(0,255),random.randint(0,255),random.randint(0,255))

t.colormode(255)
tim = t.Turtle()
tim.speed(speed="fastest")

for angle in range(int(360/5)):
  tim.pencolor(random_color())
  tim.circle(100)
  tim.setheading(tim.heading() + 5)


screen = t.Screen()
screen.exitonclick()