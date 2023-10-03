from turtle import Turtle
MOVE_SPEED = 10

class Ball(Turtle):
  def __init__(self):
    super().__init__()
    self.shape("circle")
    self.color("blue")
    self.shapesize(stretch_len=0.75, stretch_wid=0.75)
    self.penup()
    self.move_speed = 0.1
    self.xdirection = 1
    self.ydirection = 1

  def hits_top_wall(self):
    if self.ycor() == 280 or self.ycor() == -280:
      return True
    return False
  
  def change_direction_y(self):
    self.ydirection *=-1

  def change_direction_x(self):
    self.xdirection *=-1
    self.move_speed *=0.80

  def hits_paddle(self, left_paddle, right_paddle):
    if self.distance(right_paddle) < 50 and self.xcor() > 320 or self.distance(left_paddle) < 50 and self.xcor() < -320:
      return True
    return False
  
  def refresh(self):
    self.home()
    self.change_direction_x()
    self.move_speed = 0.1

  def head_to_loser(self, ball_xcor):
    if ball_xcor > 0: # the scorer is the left side
      self.xdirection = 1
    else:
      self.xdirection = -1

  def move(self):
    self.goto(self.xcor()+(10*self.xdirection),self.ycor()+(10*self.ydirection))