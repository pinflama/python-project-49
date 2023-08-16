from random import randint


GAME_RULES = 'Answer "yes" if the number is even, otherwise answer "no".'

MIN_RANDOM_NUMBER = 1
MAX_RANDOM_NUMBER = 100


def is_even(random_number: int):

    return random_number % 2 == 0


def generate_game_data():

    random_number = randint(MIN_RANDOM_NUMBER, MAX_RANDOM_NUMBER)
    computer_question = f'{random_number}'

    target_result = 'yes' if is_even(random_number) else 'no'

    return computer_question, str(target_result)
