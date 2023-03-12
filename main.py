from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
from data import question_data
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)


def make_5_foods():
    """
    Make 5 foods with different colors
    :return: a list that contains five food objects
    """
    five_object = []
    first_choice = Food()
    first_choice.color("green")
    five_object.append(first_choice)
    second_choice = Food()
    second_choice.color("red")
    five_object.append(second_choice)
    third_choice = Food()
    third_choice.color("yellow")
    five_object.append(third_choice)
    fourth_choice = Food()
    fourth_choice.color("purple")
    five_object.append(fourth_choice)
    fifth_choice = Food()
    fifth_choice.color("blue")
    five_object.append(fifth_choice)
    return five_object

question_answer = question_data[0]["Answer"]
print(question_answer)


# with open("data.py") as data:
#     question = data.read()
#     print(question_dict["Answer"])

# five_colors_objects = make_5_foods()
# for food in five_colors_objects:
#     food

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
