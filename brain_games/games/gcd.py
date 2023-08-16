import math
from random import randint


GAME_RULES = 'Find the greatest common divisor of given numbers.'

MIN_RANDOM_NUMBER = 1
MAX_RANDOM_NUMBER = 100


def generate_game_data():

    random_number1 = randint(MIN_RANDOM_NUMBER, MAX_RANDOM_NUMBER)
    random_number2 = randint(MIN_RANDOM_NUMBER, MAX_RANDOM_NUMBER)
    computer_question = f'{random_number1} {random_number2}'

    target_result = math.gcd(random_number1, random_number2)

    return computer_question, str(target_result)
