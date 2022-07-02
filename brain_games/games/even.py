from random import randint

TASK_TEXT = 'Answer "yes" if the number is even, otherwise answer "no".'
START = 1
END = 100


def is_even(number):
    return number % 2 == 0


def task_data():
    question = randint(START, END)
    correct_answer = 'yes' if is_even(question) else 'no'
    return question, correct_answer
