from random import randint


GAME_RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'

MIN_RANDOM_NUMBER = 1
MAX_RANDOM_NUMBER = 100


def is_prime(random_number) -> bool:

    if random_number <= 1:
        return False

    for i in range(2, int(random_number ** 0.5 + 1)):
        if random_number % i == 0:
            return False

    return True


def generate_game_data():

    random_number = randint(MIN_RANDOM_NUMBER, MAX_RANDOM_NUMBER)
    computer_question = f'{random_number}'

    target_result = 'yes' if is_prime(random_number) else 'no'

    return computer_question, target_result
