from random import randint

TASK_TEXT = "Find the greatest common divisor of given numbers."
START = 1
END = 100


def is_correct(player_task):
    (first_num, second_num) = player_task
    temp = first_num if first_num > second_num else second_num
    for i in range(1, temp + 1):
        if (first_num % i == 0) and (second_num % i == 0):
            return str(i)


def task_data():
    question_data = randint(START, END), randint(START, END)
    (first_num, second_num) = question_data
    question = f'{first_num} {second_num}'
    correct_answer = is_correct(question_data)
    return question, correct_answer
