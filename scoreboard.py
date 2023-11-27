from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(-360, 360)

    def update_scoreboard(self):
        self.write(f"Score: {self.score}", False, "left", ("Verdana", 20, "normal"))

    def player_score(self):
        self.score += 100
        self.clear()
        self.update_scoreboard()