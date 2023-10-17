from turtle import Turtle

ALIGNMENT = "center"
FONT = ("century", 72, "bold")

class ScoreBoard(Turtle):
    def __init__(self,):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("LimeGreen")
        self.sety(200)
        self.right_score = 0
        self.left_score = 0
        self.scoreboard_score()

    def scoreboard_score(self):
        self.clear()
        self.write(f"{self.left_score}:{self.right_score}", align=ALIGNMENT, font=FONT)

    def right_point(self):
        self.right_score += 1
        self.scoreboard_score()

    def left_point(self):
        self.left_score += 1
        self.scoreboard_score()

    def game_over(self):
        self.sety(0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)
