from random import randint

import prompt

TASK_TEXT = 'Answer "yes" if the number is even, otherwise answer "no".'
ANSWER_TEXT = 'Your answer: '
ATTEMPTS_COUNT = 3
START = 1
END = 100


def welcome_player():
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def is_correct(player_answer, player_task):
    correct_answer = 'yes' if is_even(player_task) else 'no'
    return correct_answer == player_answer, correct_answer


def is_even(number):
    return number % 2 == 0


def task():
    return randint(START, END)


def game():
    player_name = welcome_player()
    current_attempt = 1
    print(TASK_TEXT)
    while current_attempt <= ATTEMPTS_COUNT:
        player_task = task()
        print(f"Question: {player_task}")
        player_answer = prompt.string(ANSWER_TEXT)
        (correct, correct_answer) = is_correct(player_answer, player_task)
        if not correct:
            print(f"{player_answer} is wrong answer ;(. Correct answer was {correct_answer}.")
            print(f"Let's try again, {player_name}!")
            return
        print('Correct!')
        current_attempt += 1
    print(f"Congratulations, {player_name}!")


def main():
    game()


if __name__ == '__main__':
    main()
