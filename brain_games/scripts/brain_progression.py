from random import randint

import prompt

TASK_TEXT = "What number is missing in the progression?"
ANSWER_TEXT = 'Your answer: '
ATTEMPTS_COUNT = 3
START = 1
END = 100


def welcome_player():
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def is_correct(player_answer, player_task):
    return player_answer == str(player_task), player_task


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
            line += f".."
            secret_num = first_num
        else:
            first_num += step_num
            line += f"{first_num}"
        line += ' '
        i += 1
    return line.strip(), secret_num


def game():
    player_name = welcome_player()
    current_attempt = 1
    print(TASK_TEXT)
    while current_attempt <= ATTEMPTS_COUNT:
        (line, answer) = task()
        print(f"Question: {line} ")
        player_answer = prompt.string(ANSWER_TEXT)
        (correct, correct_answer) = is_correct(player_answer, answer)
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
