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
    with open("day20-21-snakegame\data.txt") as file:
      self.high_score = int(file.read())
    self.goto(0,265)
    self.update_score()

  def update_score(self):
    self.clear()
    self.write(f"Score: {self.score}, High Score: {self.high_score}", move=False, align=ALIGNMENT, font=FONT)

  # def game_over(self):
  #   self.goto(0,0)
  #   self.write("GAME OVER!", align = ALIGNMENT, font = FONT)
  
  def reset(self):
    if self.score > self.high_score:
      self.high_score = self.score
      with open("day20-21-snakegame\data.txt", mode = "w") as file:
        file.write(str(self.high_score))
    self.score = 0
    self.update_score()
    
  def score_point(self):
    self.score +=1
    self.update_score()
