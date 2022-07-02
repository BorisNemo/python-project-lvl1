from random import randint

TASK_TEXT = "Find the greatest common divisor of given numbers."
START = 1
END = 100


def is_correct(player_task):
    answer = 0
    (a, b) = player_task
    if a > b:
        temp = a
    else:
        temp = b
    for i in range(1, temp + 1):
        if (a % i == 0) and (b % i == 0):
            answer = str(i)
    return answer


def task_data():
    question_data = randint(START, END), randint(START, END)
    (first_num, second_num) = question_data
    question = f'{first_num} {second_num}'
    correct_answer = is_correct(question_data)
    return question, correct_answer
