import prompt


GAME_ATTEMPTS = 3


def run_game(game):

    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, {}!'.format(name))
    print(game.GAME_RULES)

    for game_round in range(GAME_ATTEMPTS):
        computer_question, target_result = game.generate_game_data()
        print(f'Question: {computer_question}')
        user_answer = prompt.string('Your answer: ')

        if target_result != user_answer.lower():
            print(
                f"'{user_answer}' is wrong answer ;(.",
                f"Correct answer was '{target_result}'.",
            )
            print(f"Let's try again, {name}!")
            break

        else:
            print('Correct!')
    else:
        print('Congratulations, {}!'.format(name))
