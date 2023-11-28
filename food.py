import random
from turtle import Turtle
import time

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("blue")
        self.penup()
        self.speed("slow")
        self.y_move = -10
        self.move_speed = 0.05


    def move(self):
        time.sleep(self.move_speed)
        new_x = self.xcor()
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)
    # detect horizontal collision
    # multiplied y_move for -1 to get the opposite negative number, so the ball travels in the other direction

    def refresh_position(self, xposition, yposition):
        self.showturtle()
        self.goto(xposition, yposition)
        self.move_speed = 0.05
        self.move()
