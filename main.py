import game
import printer

file_word = './data/words.csv'

print('Добро пожаловать в игру "Виселица"!\n')

printer.print_manual()

print('\nВы желаете начать новую игру?[Y/n]:')
is_game_start = input('> ').lower()

while is_game_start == 'y':
    word = game.get_random_word(file_word)
    game_state = game.init_game_state(word)

    while not game.is_end_of_game(game_state):
        printer.draw_gibbet(game_state)
        printer.print_current_revealed_chars(game_state)
        printer.print_remaining_attempts(game_state)
        
        print(f'Введите следующую буву:')
        assumed_letter = input('> ')
        code, move_result_msg = game.process_move(assumed_letter, game_state)
        print(move_result_msg)
        print('Press enter to continue')
        input()
        print('_'*30)

    printer.draw_gibbet(game_state)
    print(game.get_game_summary(game_state)[1])

    print('Вы желаете начать новую игру?[Y/n]:')
    is_game_start = input('> ').lower()
