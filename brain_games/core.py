import prompt


ANSWER_TEXT = 'Your answer: '
ATTEMPTS_COUNT = 3


def welcome_player():
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def game(data):
    print('Welcome to the Brain Games!')
    player_name = welcome_player()
    task_text = data.TASK_TEXT
    current_attempt = 1
    print(task_text)
    while current_attempt <= ATTEMPTS_COUNT:
        question, correct_answer = data.task_data()
        print(f"Question: {question}")
        player_answer = prompt.string(ANSWER_TEXT)
        if correct_answer != player_answer:
            print(f"{player_answer} is wrong answer ;(. Correct answer "
                  f"was {correct_answer}.")
            print(f"Let's try again, {player_name}!")
            return
        print('Correct!')
        current_attempt += 1
    print(f"Congratulations, {player_name}!")
