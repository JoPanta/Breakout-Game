import turtle
from turtle import Turtle, Screen
from paddle import Paddle
from wall import Wall
from ball import Ball
import time
from scoreboard import Scoreboard

# setting the screen
screen = Screen()
screen.setup(width=800, height=800)
screen.bgcolor("black")
screen.title("Arkanoid")
screen.tracer(0)

scoreboard = Scoreboard()
# setting the paddle

paddle = Paddle(0, -350)

# setting the obstacles
obstacles = []
for f in range(4):
    y = 40 * f
    for i in range(12):
        x = 66 * i
        obstacle = Wall(-351 + x, 280 - y)
        obstacles.append(obstacle)


# setting the ball
ball = Ball()


screen.listen()
screen.onkeypress(paddle.move_left, "Left")
screen.onkeypress(paddle.move_right, "Right")


game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    for obstacle in obstacles:
        if ball.distance(obstacle) < 35:
            print("hit")
            ball.bounce_y()
            obstacle.hideturtle()
            obstacles.remove(obstacle)
            scoreboard.player_score()
    if ball.ycor() > 390:
        ball.bounce_y()
    if ball.xcor() > 380 or ball.xcor() < -380:
        ball.bounce_x()
    if ball.distance(paddle) < 25:
        print(ball.distance(paddle))
        ball.bounce_y()
    if len(obstacles) == 0:
        turtle.write("VICTORY")



screen.exitonclick()