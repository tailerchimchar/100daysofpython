from turtle import Turtle
import time
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
      super().__init__()
      self.color("black")
      self.penup()
      self.hideturtle()
      self.level = 1
      self.goto(-250, 250)
      self.update_score()
      
    def update_score(self):
      self.clear()
      self.goto(-250, 250)
      self.write(f"Level: {self.level}", font=FONT)
      
    def game_over(self):
      self.goto(-50,0)
      self.write("GAME OVER", font = FONT)
      
    def level_up(self):
      self.level+=1
      self.update_score()
      time.sleep(1.5)
    