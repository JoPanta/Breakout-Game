from turtle import Turtle


class Lives(Turtle):

    def __init__(self):
        super().__init__()
        self.lives = 3
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(250, 360)

    def update_lives(self):
        self.write(f"Lives: {self.lives}", False, "left", ("Verdana", 20, "normal"))

    def player_lives(self):
        self.lives -= 1
        self.clear()
        self.update_lives()