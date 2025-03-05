import game
import printer
import input_handler

file_word = './data/words.csv'

printer.out_greetings()
printer.out_manual()

printer.suggest_to_start_game()

user_choice = input_handler.get_user_choice()

while user_choice:
    word = game.get_random_word(file_word)
    game_state = game.init_game_state(word)

    while not game.is_end_of_game(game_state):
        printer.draw_gibbet(game_state)
        printer.out_current_revealed_chars(game_state)
        printer.out_remaining_attempts(game_state)
        
        printer.suggest_input_letter()       
        assumed_letter = input_handler.get_assumed_letter()
        code, move_result_msg = game.process_move(assumed_letter, game_state)
        printer.out_move_results(move_result_msg)
        printer.suggest_to_continue()
        input()
        printer.out_horizontal_separator()
        

    printer.draw_gibbet(game_state)
    
    printer.out_game_summary(game.is_win(game_state), game_state)
    

    printer.suggest_to_start_game()
    user_choice = input_handler.get_user_choice()
