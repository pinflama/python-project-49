from random import randint, choice
from operator import add, sub, mul

GAME_RULES = 'What is the result of the expression?'

MIN_RANDOM_NUMBER = 1
MAX_RANDOM_NUMBER = 100


def generate_game_data():
    
    random_number1 = randint(MIN_RANDOM_NUMBER, MAX_RANDOM_NUMBER)
    random_number2 = randint(MIN_RANDOM_NUMBER, MAX_RANDOM_NUMBER)
    operation, func = choice([("+", add), ("-", sub), ("*", mul)])
    computer_question = f'{random_number1} {operation} {random_number2}'

    target_result = func(random_number1, random_number2)

    return computer_question, str(target_result)
