from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = -1
        self.goto(0, 280)
        self.color("cyan")
        self.hideturtle()
        self.penup()

    def game_over(self):
        self.color("white")
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=("Arial", 40, "normal"))

    def score_count(self):
        self.clear()
        self.score += 1
        self.write(f"Score: {self.score}", align="center", font=("Arial", 12, "normal"))



