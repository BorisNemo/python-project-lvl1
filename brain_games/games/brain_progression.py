from random import randint


TASK_TEXT = "What number is missing in the progression?"
START = 1
END = 100


def is_correct(player_task):
    return player_task


def task():
    min_steps_num = 5
    max_steps_num = 10
    first_num = randint(START, END)
    step_num = randint(START, END)
    steps_count = randint(min_steps_num, max_steps_num)
    line = ''
    i = 0
    i_secret = randint(0, steps_count)
    secret_num = 0
    while i <= steps_count:
        if i_secret == i:
            first_num += step_num
            line += ".."
            secret_num = first_num
        else:
            first_num += step_num
            line += f"{first_num}"
        line += ' '
        i += 1
    return line.strip(), str(secret_num)


def task_data():
    question, correct_answer = task()
    return question, correct_answer
