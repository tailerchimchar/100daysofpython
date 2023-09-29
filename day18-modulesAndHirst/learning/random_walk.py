import turtle as t
import random

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return (r,g,b)

# Random walk

tim = t.Turtle()
tim.pensize(10)
t.colormode(255)
tim.speed(speed="fastest")
for i in range(250):
    tim.pencolor(random_color())
    angle = int(random.randint(1,4) * 90)
    tim.right(angle)
    tim.fd(30)

screen = t.Screen()
screen.exitonclick()