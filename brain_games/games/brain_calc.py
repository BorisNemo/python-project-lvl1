from random import randint, choice

import prompt

TASK_TEXT = "What is the result of the expression?"
START = 1
END = 100


def welcome_player():
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def is_correct(player_task):
    answer = ''
    (a, operation, b) = player_task
    if operation == '+':
        answer = str(a + b)
    elif operation == '*':
        answer = str(a * b)
    elif operation == '-':
        answer = str(a - b)
    return answer


def task():
    return


def task_data():
    question_data = randint(START, END), choice(['+', '-', '*']), randint(START, END)
    (a, operation, b) = question_data
    question = f"{a} {operation} {b}"
    correct_answer = is_correct(question_data)
    return question, correct_answer
