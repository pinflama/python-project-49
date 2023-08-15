from typing import NoReturn

import prompt


GAME_ATTEMPTS = 3


def run_game(game) -> NoReturn:
    # Приветствуем пользователя
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, {}!'.format(name))

    # Выводим правила игры, формируем логику игры и генерируем цикл раундов
    print(game.GAME_RULES)

    for game_round in range(GAME_ATTEMPTS):
        computer_question, target_result = game.generate_game_data()
        print(f'Question: {computer_question}')
        user_answer = prompt.string('Your answer: ')

        if str(target_result) != user_answer.lower():
            # Исполняется, если последний введенный ответ - неправильный
            print(
                f"'{user_answer}' is wrong answer ;(.",
                f"Correct answer was '{target_result}'.",
            )
            print(f"Let's try again, {name}!")
            break

        else:
            # Исполняется, если последний введенный ответ - правильный
            print('Correct!')

            if game_round == GAME_ATTEMPTS - 1:
                print('Congratulations, {}!'.format(name))
