from turtle import Turtle

class Choice(Turtle):

    def __init__(self, text):
        super().__init__()
        self.text = text
        self.goto(-290, 340)
        self.color("white")
        self.write(text, font=("Verdana", 12, "normal"))
        self.penup()
        self.hideturtle()