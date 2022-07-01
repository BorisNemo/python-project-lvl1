from random import randint, choice

import prompt

TASK_TEXT = "What is the result of the expression?"
ANSWER_TEXT = 'Your answer: '
ATTEMPTS_COUNT = 3
START = 1
END = 100


def welcome_player():
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def is_correct(player_answer, player_task):
    correct_answer = ''
    (a, operation, b) = player_task
    if operation == '+':
        correct_answer = str(a + b)
    elif operation == '*':
        correct_answer = str(a * b)
    elif operation == '-':
        correct_answer = str(a - b)
    return correct_answer == player_answer, correct_answer


def task():
    return randint(START, END), choice(['+', '-', '*']), randint(START, END)


def game():
    player_name = welcome_player()
    current_attempt = 1
    print(TASK_TEXT)
    while current_attempt <= ATTEMPTS_COUNT:
        (a, operation, b) = task()
        print(f"Question: {a} {operation} {b}")
        player_answer = prompt.string(ANSWER_TEXT)
        (correct, correct_answer) = is_correct(player_answer, (a, operation, b))
        if not correct:
            print(f"{player_answer} is wrong answer ;(. Correct answer was "
                  f"{correct_answer}.")
            print(f"Let's try again, {player_name}!")
            return
        print('Correct!')
        current_attempt += 1
    print(f"Congratulations, {player_name}!")


def main():
    game()


if __name__ == '__main__':
    main()
