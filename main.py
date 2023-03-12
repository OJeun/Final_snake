import turtle
from turtle import Screen, Turtle
from snake import Snake
from food import Food
from scoreboard import Scoreboard
from data import question_data
import time
import copy

import turtle
from turtle import Screen, Turtle
from snake import Snake
from food import Food
from scoreboard import Scoreboard
from data import question_data
import time
from question import Question
from choice import Choice
import copy




def generate_setting():
    setting_dict = {}
    setting_dict['first'] = 'pink'
    setting_dict['second'] = 'orange'
    setting_dict['third'] = 'yellow'
    setting_dict['fourth'] = 'blue'
    return setting_dict


def each_number_color():
    dict = generate_setting().values()
    xcor = -70
    ycor = -350
    for color in dict:
        new_turtle = Turtle()
        new_turtle.write("1")
        new_turtle.color(color)
        new_turtle.shape("circle")
        new_turtle.penup()
        new_turtle.goto(xcor, ycor)
        xcor += 30




# 여기까지가 선택지 객체 만드는 함수
def generate_turtle(setting_dict):
    select_arr = ['first', 'second', 'third', 'fourth']
    select_obj = []
    for i in range(4):
        temp_turtle = Food(select_arr[i])
        temp_turtle.color(setting_dict[select_arr[i]])
        select_obj.append(temp_turtle)

    return select_obj


def mapping_question(data, index):
    question = data[index]['Q']
    choice = data[index]['choices']
    # choice = choice.split('\n')
    # new_choice = []
    # for i in range(len(choice)):
    #     if choice[i] == '':
    #         continue
    #     else:
    #         new_choice.append(choice[i].strip())
    # choice = new_choice
    answer = data[index]['Answer']
    return question, choice, answer


# 문제를 만드는 함수
def make_question(index):
    question_text = question_data[index]["Q"]
    question = Turtle()
    question.goto(0, 380)
    question.color("white")
    question.hideturtle()
    question.write(question_text)


# 답 위치 함수
def answer_coord(correct_object):
    x = correct_object.xcor()
    y = correct_object.ycor()
    tuple_x_y = (x, y)
    return tuple_x_y


def make_line(ycor):
    line_turtle = Turtle()
    line_turtle.color("white")
    line_turtle.penup()
    line_turtle.goto(-300, ycor)
    line_turtle.pendown()
    line_turtle.goto(300, ycor)

def main():
    screen = Screen()
    screen.setup(width=600, height=870)
    screen.bgcolor("black")
    screen.title("Job Security")
    screen.tracer(0)
    snake = Snake()

    scoreboard = Scoreboard()
    make_line(310)
    make_line(-305)
    screen.listen()
    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.left, "Left")
    screen.onkey(snake.right, "Right")

    each_number_color()
    setting_dict = generate_setting()
    select_turtle = generate_turtle(setting_dict)
    # main()
    index = 0
    # 1차적으로 일단 우리는 답에 대한 초기값을 설정합니다.
    # First, we set correct answer and question.
    question, choice, answer = mapping_question(question_data, index)
    # 첫번째 질문에 대한 답은 2번 초기값을 답 2로 매칭시켜버렸다.

    question_turtle = Question(question)
    choice_turtle = Choice(choice)

    game_is_on = True
    while game_is_on:
        # 움직인닷!
        screen.update()
        time.sleep(0.1)
        snake.move()
        correct_object = select_turtle[answer - 1]
        # 어렵게 가지 말자
        incorrect_object = []

        for i, value in enumerate(select_turtle):
            if i == answer - 1:
                continue
            else:
                incorrect_object.append(value)

        # 결국 뱀의 머리가 정답간의 거리가 15 이하일 때 정답으로 체크
        if snake.head.distance(correct_object) < 15:
            time.sleep(1.5)
            index += 1
            question, choice, answer = mapping_question(question_data, index)
            scoreboard.increase_game()
            for i in select_turtle:
                i.refresh()

            question_turtle.clear()
            choice_turtle.clear()

            question_turtle.write(question, font=("Verdana", 12, "normal"))
            choice_turtle.write(choice, font=("Verdana", 10, "normal"))
            snake.extend()
            scoreboard.increase_score()

        for i in incorrect_object:
            if snake.head.distance(i) < 15:
                snake.extend()
                scoreboard.decrease_score()

        if scoreboard.score < -100:
            scoreboard.reset()
            snake.remove_snake()
            scoreboard.game_over()

        if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
            scoreboard.reset()
            snake.remove_snake()
            scoreboard.game_over()
            # snake.reset()

        if scoreboard.question == 10:
            scoreboard.reset()
            snake.remove_snake()
            scoreboard.all_questions_finished()

        # Detect collision with tail.
        for segment in snake.segments:
            if segment == snake.head:
                pass
            elif snake.head.distance(segment) < 10:
                scoreboard.reset()
                snake.remove_snake()
                scoreboard.game_over()
                snake.reset()


# screen.exitonclick()
if __name__ == "__main__":
    is_user_yes = True
    while is_user_yes:
        print("\n"
              "This snake game is to to help you get a job! \n"
              "We have 10 questions that will informative for helping your job hunting.\n"
              "You can see the question and choices above, and read it as fast as you can! \n"
              "You can see five balls with different colors and each ball points the each choice\n"
              "There will be only one ball that points to correct answer\n"
              "On the bottom, the order of colors is choices 1, 2, 3, 4\n"
            )
        user_answer = input("Do you want to get a dream job? Yes or no : ")
        if user_answer.title() == "Yes":
            is_user_yes = False

            main()

        elif user_answer.title() == "No":
            user_answer = input("I think you want to play this game, Yes or No")


