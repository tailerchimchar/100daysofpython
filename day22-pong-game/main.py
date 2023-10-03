from turtle import Turtle, Screen
import paddle
import time
from ball import Ball
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)
screen.listen()

right_paddle = paddle.Paddle(350, 0)
left_paddle = paddle.Paddle(-350, 0)
ball = Ball()
scoreboard = Scoreboard()

screen.onkey(right_paddle.move_up, 'Up')
screen.onkey(right_paddle.move_down, 'Down')

screen.onkey(left_paddle.move_up, 'w')
screen.onkey(left_paddle.move_down, 's')

game_is_on = True
while game_is_on:
  time.sleep(ball.move_speed)
  ball.move()

  # detect top wall collision
  if ball.hits_top_wall():
    ball.change_direction_y()
  screen.update()

  # detect collision with paddles
  if ball.hits_paddle(left_paddle=left_paddle, right_paddle=right_paddle):
    ball.change_direction_x()
 
  # detect if ball goes out of bounds
  if ball.xcor() > 400:
    ball.refresh()
    scoreboard.l_point()

  if ball.xcor() < -400:
    ball.refresh()
    scoreboard.r_point()


screen.exitonclick()