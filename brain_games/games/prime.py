from random import randint


TASK_TEXT = 'Answer "yes" if given number is prime. Otherwise answer "no".'
START = 1
END = 100


def is_correct(player_task):
    correct_answer = 'yes' if is_prime(player_task) else 'no'
    return correct_answer


def is_prime(num):
    counter = 2
    while num % counter != 0:
        counter += 1
        if counter == num:
            return True
    return False


def task_data():
    question = randint(START + 1, END)
    correct_answer = is_correct(question)
    return question, correct_answer
