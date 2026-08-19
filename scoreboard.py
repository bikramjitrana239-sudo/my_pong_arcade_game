from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self, fire, water):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.fire = fire
        self.water = water

    def l_point(self):
        self.l_score += 1
        self.update_scoreboard()

    def r_point(self):
        self.r_score += 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 200)
        self.color(self.water[1])
        self.write(f"{self.water[0]} {self.l_score}", align="center", font=("Courier", 20, "normal"))
        self.goto(100, 200)
        self.color(self.fire[1])
        self.write(f"{self.fire[0]} {self.r_score}", align="center", font=("Courier", 20, "normal"))

    def game_over(self):
        self.goto(0, -200)
        self.color("white")
        self.write("Game Over!", align="center", font=("Courier", 30, "normal"))