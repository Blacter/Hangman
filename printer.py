def print_current_revealed_chars(game_state: dict) -> None:
    for c in game_state['revealed_word_chars']:
        print(c, end="")
    print()

    return None


def print_manual():
    print('Для победы в игре отгадайте слово путем подбора букв.')
    print('Изначально открыты несколько букв слова.')
    print('Изначально открытая буква может быть скрыта в другой позиции в слове.')
    print('Всего вы можете допустить 6 неудачных попыток.')


def print_remaining_attempts(game_state: dict) -> None:
    print('Количество оставшихся попыток: ', end='')
    print(game_state['max_attempts'] - game_state['player_attempts_done'])
    

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
