from turtle import Turtle

class Paddle(Turtle):

  def __init__(self, xcor, ycor):
    super().__init__()
    self.width = 20
    self.shape("square")
    self.hideturtle()
    self.shapesize(stretch_len=1, stretch_wid=5)
    self.color("white")
    self.penup()
    self.goto(xcor, ycor)
    self.showturtle()

  def move_up(self):
    self.goto(self.xcor(), self.ycor() + 15)

  def move_down(self):
    self.goto(self.xcor(), self.ycor() - 15)