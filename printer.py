from string import Template

greetings = 'Добро пожаловать в игру "Виселица"!\n'

manual_1 = 'Для победы в игре отгадайте слово путем подбора букв.\n'
manual_2 = 'Изначально открыты несколько букв слова.\n'
manual_3 = 'Изначально открытая буква может быть скрыта в другой позиции в слове.\n'
manual_4 = 'Всего вы можете допустить 6 неудачных попыток.'

start_new_game_suggestion = '\nВы желаете начать новую игру?[Y/n]:'

remaining_attempts = Template('Количество оставшихся попыток: $n1')

win_summary = Template('Победа! Вы отгадали все буквы! Полученное слово: $n1.')
lose_summary = 'Ваши попытки закончились. Вы проиграли'

input_letter_suggestion = 'Введите следующую буву:'

continue_suggestion = 'Press enter to continue ...'
horizontal_separator = '_'*30

def out_current_revealed_chars(game_state: dict) -> None:
    for c in game_state['revealed_word_chars']:
        print(c, end="")
    print()

    return None


def out_greetings() -> None:
    print(greetings)


def out_manual() -> None:
    print(manual_1 + manual_2 + manual_3 + manual_4)


def suggest_to_start_game() -> None:
    print(start_new_game_suggestion)


def out_remaining_attempts(game_state: dict) -> None:
    print(remaining_attempts.substitute(
        n1=game_state['max_attempts'] - game_state['player_attempts_done']))


def out_win_summary(game_state: dict) -> None:
    print(win_summary.substitute(
        n1=''.join(game_state["revealed_word_chars"])))


def out_lose_summary() -> None:
    print(lose_summary)


def out_game_summary(is_win: bool, game_state: dict) -> None:
    if is_win:
        out_win_summary(game_state)
    else:
        out_lose_summary()


def suggest_input_letter() -> None:
    print(input_letter_suggestion)


def out_move_results(move_result_msg: str) -> None:
    print(move_result_msg)


def suggest_to_continue() -> None:
    print(continue_suggestion)


def out_horizontal_separator() -> None:
    print(horizontal_separator)
    # print('_'*30)


def draw_gibbet(game_state: dict) -> None:
    '''Draw gibbet consolas'''

    if game_state['player_attempts_done'] == 0:
        print(f' /')
        print(f' |')
        print(f' |')
        print(f' |')
        print(f' |')
        print(f' |')
        print(f' |')
        print(f' |')
        print(f' |')
        print(f' |')
        print(f' {"-"*18}')
    elif game_state['player_attempts_done'] == 1:
        print(f' /-------v----------\\')
        print(f' |')
        print(f' |')
        print(f' |')
        print(f' |')
        print(f' |')
        print(f' |')
        print(f' |')
        print(f' |')
        print(f' |')
        print(f' {"-"*18}')
    elif game_state['player_attempts_done'] == 2:
        print(f' /-------v----------\\')
        print(f' |       |')
        print(f' |       |')
        print(f' |')
        print(f' |')
        print(f' |')
        print(f' |')
        print(f' |')
        print(f' |')
        print(f' |')
        print(f' {"-"*18}')

    elif game_state['player_attempts_done'] == 3:
        print(f' /-------v----------\\')
        print(f' |       |')
        print(f' |       |')
        print(f' |       0')
        print(f' |')
        print(f' |')
        print(f' |')
        print(f' |')
        print(f' |')
        print(f' |')
        print(f' {"-"*18}')

    elif game_state['player_attempts_done'] == 4:
        print(f' /-------v----------\\')
        print(f' |       |')
        print(f' |       |')
        print(f' |       0')
        print(f' |       |')
        print(f' |       @')
        print(f' |       @')
        print(f' |')
        print(f' |')
        print(f' |')
        print(f' {"-"*18}')
    elif game_state['player_attempts_done'] == 5:
        print(f' /-------v----------\\')
        print(f' |       |')
        print(f' |       |')
        print(f' |     \\ 0 /')
        print(f' |      \\|/ ')
        print(f' |       @  ')
        print(f' |       @  ')
        print(f' |')
        print(f' |')
        print(f' |')
        print(f' {"-"*18}')

    elif game_state['player_attempts_done'] == 6:
        print(f' /-------v----------\\')
        print(f' |       |')
        print(f' |       |')
        print(f' |     \\ 0 /')
        print(f' |      \\|/ ')
        print(f' |       @  ')
        print(f' |       @  ')
        print(f' |      / \\ ')
        print(f' |     /   \\ ')
        print(f' |')
        print(f' {"-"*18}')


if __name__ == '__main__':
    game_state_short = {
        'player_attempts_done': 0
    }
    print(f'{game_state_short["player_attempts_done"]=}')
    draw_gibbet(game_state_short)

    game_state_short = {
        'player_attempts_done': 1
    }
    print(f'{game_state_short["player_attempts_done"]=}')
    draw_gibbet(game_state_short)

    game_state_short = {
        'player_attempts_done': 2
    }
    print(f'{game_state_short["player_attempts_done"]=}')
    draw_gibbet(game_state_short)

    game_state_short = {
        'player_attempts_done': 3
    }
    print(f'{game_state_short["player_attempts_done"]=}')
    draw_gibbet(game_state_short)

    game_state_short = {
        'player_attempts_done': 4
    }
    print(f'{game_state_short["player_attempts_done"]=}')
    draw_gibbet(game_state_short)

    game_state_short = {
        'player_attempts_done': 5
    }
    print(f'game_state_short["player_attempts_done"]=')
    draw_gibbet(game_state_short)

    game_state_short = {
        'player_attempts_done': 6
    }
    print(f'{game_state_short["player_attempts_done"]=}')
    draw_gibbet(game_state_short)
    # print(f' /------\\')
    # print(f' |   |')
    # print(f' |   |')
    # print(f' | \\ 0 /')
    # print(f' |  \\|/ ')
    # print(f' |   @  ')
    # print(f' |   @  ')
    # print(f' |  / \\ ')
    # print(f' | /   \\ ')
    # print(f' |')
    # print(f' {"-"*11}')
