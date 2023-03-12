from turtle import Turtle

class Question(Turtle):

    def __init__(self, text):
        super().__init__()
        self.text = text
        self.goto(-290, 390)
        self.color("white")
        self.write(text, font=("Verdana", 15, "normal"))
        self.penup()
        self.hideturtle()


