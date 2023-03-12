from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.question = 1
        # with open("data.txt") as data:
        #     self.high_score = int(data.read())
        self.color("white")
        self.penup()
        self.goto(0, 280)
        self.hideturtle()
        self.update_scoreboard()


    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} Question: {self.question}/10", align=ALIGNMENT, font=FONT)

    def reset(self):
        # if self.score > self.high_score:
        #     self.high_score = self.score
        #     with open("data.txt", mode="w") as data:
        #         data.write(f"{self.high_score}")
        self.score = 0
        self.clear()
        self.update_scoreboard()

    def increase_game(self):
        self.question += 1
        self.update_scoreboard()
    def game_over(self):
        self.goto(0, 0)
        self.clear()
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)
    def all_questions_finished(self):
        self.goto(0, 0)
        self.clear()
        self.write("You must get a job with 100%", align=ALIGNMENT, font=FONT)
    def increase_score(self):
        self.score += 100
        self.update_scoreboard()

    def decrease_score(self):
        self.score -= 50
        self.update_scoreboard()
