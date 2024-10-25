from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("20Proyecto\score.txt", mode="r") as file:
            self.highestScore = int(file.read())
        self.color("white")
        self.penup()
        self.goto(x=0, y=270)
        self.updateScore()
        self.hideturtle()

    def updateScore(self):
        self.clear()
        self.write(
            f"Score = {self.score}, Highest Score: {self.highestScore}",
            align="center",
            font=("Arial", 14, "normal"),
        )

    def reset(self):
        if self.score > self.highestScore:
            self.highestScore = self.score
            with open("20Proyecto\score.txt", mode="w") as file:
                file.write(f"{self.highestScore}")
        self.score = 0
        self.updateScore()

    # def GameOver(self):
    #     self.goto(x=0, y=0)
    #     self.write(
    #         f"Score = {self.score}",
    #         align="center",
    #         font=("Arial", 14, "normal"),
    #     )

    def increaseScore(self):
        self.score += 1
        self.updateScore()
