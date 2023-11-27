import random
from turtle import Turtle

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("blue")
        self.penup()
        self.speed("slow")
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.05

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    # detect horizontal collision
    # multiplied y_move for -1 to get the opposite negative number, so the ball travels in the other direction

    def bounce_y(self):
        self.y_move *= -1

    # detect horizontal collision
    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 0.8

    def refresh_position(self):
        self.goto(0, 0)
        self.move_speed = 0.05
        self.bounce_x()
        self.move()
