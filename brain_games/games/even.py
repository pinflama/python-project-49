from random import randint
from typing import Callable

GAME_RULES = 'Answer "yes" if the number is even, otherwise answer "no".'

MIN_RANDOM_NUMBER = 1
MAX_RANDOM_NUMBER = 100


def is_even(random_number: int) -> tuple:

    return True if random_number % 2 == 0 else False


def generate_game_data() -> tuple:
    # Генерируем данные и задаем вопрос пользователю
    random_number = randint(MIN_RANDOM_NUMBER, MAX_RANDOM_NUMBER)
    computer_question = f'{random_number}'

    # Определяем правильный ответ
    target_result = 'yes' if is_even(random_number) else 'no'

    return computer_question, target_result
