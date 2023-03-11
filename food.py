from turtle import *
import random


# Food inherit Turtle class
class Food(Turtle):

    def __init__(self):
        # super == parent object
        super().__init__()
        # By adding __init__, we can use method and attribute of turtle class
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
        self.refresh()
        # self.color('deep pink')
        # self.penup()
        # self.style = ('Courier', 30, 'italic')
        # self.write('Hello!', align='center')
        # self.hideturtle()
        # self.shape("circle")
        # self.penup()
        # self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        # self.color("blue")
        # self.speed("fastest")
        # self.refresh()

    def refresh(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)
