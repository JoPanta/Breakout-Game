from turtle import Turtle, Screen
from paddle import Paddle
from wall import Wall

# setting the screen
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Arkanoid")
screen.tracer(0)


# setting the paddle

paddle = Paddle(0, -260)

# setting the little walls
for f in range(5):
    y = 40 * f
    for i in range(8):
        x = 99 * i
        wall = Wall(-351 + x, 280 - y)


screen.listen()
screen.onkeypress(paddle.move_left, "Left")
screen.onkeypress(paddle.move_right, "Right")


game_is_on = True

while game_is_on:
    screen.update()



screen.exitonclick()