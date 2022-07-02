from random import randint

TASK_TEXT = 'Answer "yes" if the number is even, otherwise answer "no".'
START = 1
END = 100


def is_correct(player_task):
    return 'yes' if is_even(player_task) else 'no'


def is_even(number):
    return number % 2 == 0


def task_data():
    question = randint(START, END)
    correct_answer = is_correct(question)
    return question, correct_answer
