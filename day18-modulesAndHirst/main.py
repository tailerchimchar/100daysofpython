import turtle as t
import random

color_list = [(240, 246, 243), (132, 166, 205), (221, 148, 106), (32, 42, 61), (199, 135, 148), (166, 58, 48), (141, 184, 162), (39, 105, 157), (237, 212, 90), (150, 59, 66), (216, 82, 71), (168, 29, 33), (235, 165, 157), (51, 111, 90), (35, 61, 55), (156, 33, 31), (17, 97, 71), (52, 44, 49), (230, 161, 166), (170, 188, 221), (57, 51, 48), (184, 103, 113), (32, 60, 109), (105, 126, 159), (175, 200, 188), (34, 151, 210), (65, 66, 56)]
screen = t.Screen()

t.colormode(255)
tim = t.Turtle(shape = "turtle", visible=False)
tim.speed(speed="fastest")
tim.penup()
tim.goto(-200, -200)
tim.pendown()
tim.hideturtle()
tim.pensize(14)

def draw_row():
  for _ in range(10):
    tim.pencolor(random.choice(color_list))
    tim.pendown()
    tim.circle(7)
    tim.penup()
    tim.forward(50)

  
def move_tim(x_coord, y_coord):
  tim.goto(x_coord, y_coord)
  #tim.left(90)

def draw_hirst_painting():
  y_coord = -200
  for _ in range(10):
    x_coord = -200
    draw_row()
    y_coord+=50
    move_tim(x_coord, y_coord)

draw_hirst_painting()

screen.exitonclick()
