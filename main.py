from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import data
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

def make_5_foods():
    first_choice = Food()
    first_choice.color("green")
    second_choice = Food()
    second_choice.color("red")
    third_choice = Food()
    third_choice.color("yellow")
    fourth_choice = Food()
    fourth_choice.color("purple")
    fifth_choice = Food()
    fifth_choice.color("blue")


with open("data.py") as data:
    question = data.read()
    print(question_dict["Answer"])


snake = Snake()
food = Food()
make_5_foods()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision with food.
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()


    # Detect collision with wall.
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.reset()
        snake.remove_snake()
        scoreboard.game_over()
        # snake.reset()

    # Detect collision with tail.
    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.remove_snake()
            scoreboard.game_over()
            # snake.reset()






screen.exitonclick()
