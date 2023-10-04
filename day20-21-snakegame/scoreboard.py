from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Courier', 15, 'normal')

class Scoreboard(Turtle):
  score = 0
  def __init__(self):
    super().__init__()
    self.hideturtle()
    self.color("white")
    self.penup()
    self.score = 0
    self.goto(0,265)
    self.update_score()

  def update_score(self):
    self.write(f"Score: {self.score}", move=False, align=ALIGNMENT, font=FONT)

  def game_over(self):
    self.goto(0,0)
    self.write("GAME OVER!", align = ALIGNMENT, font = FONT)

  def score_point(self):
    self.score +=1
    self.clear()
    self.update_score()
