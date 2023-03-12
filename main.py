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

answer_object = "hi"
correct_food = "Julie"

first_choice = "1"
second_choice = "2"
third_choice = "3"
fourth_choice = "4"
fifth_choice = "5"
def make_5_foods():
    """
    Make 5 foods with different colors
    :return: a list that contains five food objects
    """
    five_object = []
    global first_choice
    first_choice = Food()
    first_choice.color("green")
    first_choice.refresh()
    five_object.append(first_choice)
    global second_choice
    second_choice = Food()
    second_choice.color("red")
    second_choice.refresh()
    five_object.append(second_choice)
    global third_choice
    third_choice = Food()
    third_choice.color("yellow")
    third_choice.refresh()
    five_object.append(third_choice)
    global fourth_choice
    fourth_choice = Food()
    fourth_choice.color("purple")
    fourth_choice.refresh()
    five_object.append(fourth_choice)
    global fifth_choice
    fifth_choice = Food()
    fifth_choice.color("blue")
    fifth_choice.refresh()
    five_object.append(fifth_choice)
    print(five_object)

    global answer_object
    answer_object = question_data[0]["Answer"]
    global correct_food
    correct_food = five_object[answer_object-1]

    return five_object


    # global answer_object
    # answer_object = question_data[0]["Answer"]
    # print(answer_object)
    # global correct_food
    # correct_food = five_object[answer_object-1]
    # print(correct_food)








def answer_coord(correct_object):
    x = correct_object.xcor()
    y = correct_object.ycor()
    tuple_x_y = (x, y)
    return tuple_x_y



# question_answer = question_data[0]["Answer"]
# print(question_answer)


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
    if snake.head.distance(correct_food) < 15:

        # food.refresh()
        # initial_foods = make_5_foods()

        first_choice.goto(1000, 1000)
        second_choice.goto(1000, 1000)
        third_choice.goto(1000, 1000)
        fourth_choice.goto(1000, 1000)
        fifth_choice.goto(1000, 1000)
        make_5_foods()

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
