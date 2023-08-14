from random import randint, choice
from typing import Callable
from operator import add, sub, mul

GAME_RULES = 'What is the result of the expression?'

MIN_RANDOM_NUMBER = 1
MAX_RANDOM_NUMBER = 100

ARITHMETIC_OPERATIONS =  [("+", add), ("-", sub), ("*", mul)]


def generate_game_data() -> tuple:
    # Генерируем данные и задаем вопрос пользователю
    random_number1 = randint(MIN_RANDOM_NUMBER, MAX_RANDOM_NUMBER)
    random_number2 = randint(MIN_RANDOM_NUMBER, MAX_RANDOM_NUMBER)
    operation, func = choice(ARITHMETIC_OPERATIONS)
    computer_question = f'{random_number1} {operation} {random_number2}'

    # Определяем правильный ответ
    target_result = func(random_number1, random_number2)

    return computer_question, str(target_result)
