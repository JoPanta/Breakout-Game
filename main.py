import turtle
from turtle import Turtle, Screen
from paddle import Paddle
from wall import Wall
from ball import Ball
import time
from scoreboard import Scoreboard
from lives import Lives
# setting the screen
tr = turtle.Turtle()
screen = Screen()
screen.setup(width=800, height=800)
screen.bgcolor("black")
screen.title("Arkanoid")
screen.tracer(0)
# screen.bgpic('raining.gif')

scoreboard = Scoreboard()
lives = Lives()
# setting the paddle

paddle = Paddle(0, -350)

# setting the obstacles
obstacles = []
for f in range(3):
    y = 40 * f
    for i in range(10):
        x = 77 * i
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
    scoreboard.update_score()
    lives.update_lives()
    screen.update()
    ball.move()
    for obstacle in obstacles:
        if ball.distance(obstacle) < 35:
            if obstacle.fillcolor() == "dark green":
                paddle.turtlesize(stretch_wid=0.5, stretch_len=7)
            if obstacle.fillcolor() == "red":
                paddle.turtlesize(stretch_wid=0.5, stretch_len=4)
            ball.bounce_y()
            obstacle.hideturtle()
            obstacles.remove(obstacle)
            scoreboard.player_score()
    if ball.ycor() > 390:
        ball.bounce_y()
    if ball.ycor() < -390:

        lives.player_lives()
        ball.refresh_position()
        if lives.lives == 0:
            game_is_on = False
            turtle.color('white')
            turtle.hideturtle()
            turtle.write('GAME OVER', align="center", font=("Verdana", 50, "normal"))
            ball.hideturtle()
    if ball.xcor() > 380 or ball.xcor() < -380:
        ball.bounce_x()
    if ball.distance(paddle) < 25:
        ball.bounce_y()
    if len(obstacles) == 0:
        game_is_on: False
        turtle.color('white')
        turtle.hideturtle()
        turtle.write('VICTORY', align="center", font=("Verdana", 50, "normal"))
        ball.hideturtle()



screen.exitonclick()