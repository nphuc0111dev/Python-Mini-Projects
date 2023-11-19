from turtle import Turtle

ALIGNMENT = "Center"
TEXT_COLOR = "white"
FONT = ("Arial", 24, "normal")


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt", "r") as file:
            self.high_score = int(file.read())
        self.color(TEXT_COLOR)
        self.speed("fast")
        self.penup()
        self.goto(0, 270)
        self.update_score()
        self.hideturtle()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score >= self.high_score:
            self.high_score = self.score
            with open("data.txt", "w") as file:
                file.write(str(self.high_score))

        self.score = 0
        self.update_score()

    def increment_score(self):
        self.score += 1
        self.clear()
        self.update_score()
    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write(f"GAME OVER", align=ALIGNMENT, font=FONT)
