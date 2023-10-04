from turtle import Turtle

STARTING_POSITION = (0, -270)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

UP=90
RIGHT=0
LEFT=180
DOWN=270

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.shapesize(stretch_len=1.25, stretch_wid=1.25)
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(UP)
        
    def move_up(self):
      self.goto(self.xcor(), self.ycor()+MOVE_DISTANCE)
      self.setheading(UP)

    def move_right(self):
      self.goto(self.xcor()+MOVE_DISTANCE, self.ycor())
      self.setheading(RIGHT)

    def move_left(self):
      self.goto(self.xcor()-MOVE_DISTANCE, self.ycor())
      self.setheading(LEFT)

    def move_down(self):
      self.goto(self.xcor(), self.ycor()-MOVE_DISTANCE)
      self.setheading(DOWN)
      
    def refresh(self):
      self.goto(STARTING_POSITION)
      
    def is_at_finish(self):
      if self.ycor() > FINISH_LINE_Y:
        return True
      return False