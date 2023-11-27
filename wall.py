from turtle import Turtle
import random

class Wall(Turtle):
    def __init__(self, xcor, ycor):
        super().__init__()
        colors = ["blue", "lime green", "yellow", "red", "dark slate blue", "medium violet red",
                  "dark green", "orange red"]
        random_color = random.choice(colors)
        self.shape("square")
        self.penup()
        self.turtlesize(stretch_wid=1, stretch_len=4)
        self.color(random_color)
        self.setposition(xcor, ycor)