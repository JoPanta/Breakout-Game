from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, xcor, ycor):
        super().__init__()
        self.shape("square")
        self.penup()
        self.turtlesize(stretch_wid=0.5, stretch_len=4)
        self.color("white")
        self.setposition(xcor, ycor)

    def move_left(self):
        new_x = self.xcor() - 30
        self.setx(new_x)

    def move_right(self):
        new_x = self.xcor() + 30
        self.setx(new_x)
