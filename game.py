import random
import csv


def get_random_word(file_with_words: str) -> str | None:
    '''Get ramdom word from file.csv'''
    with open(file_with_words, 'r', encoding='UTF-8') as f:
        reader = csv.reader(f)
        amount_words = int(next(reader)[0])
        word_number_to_return = random.randint(1, amount_words)
        for i, word in reader:
            if int(i) == word_number_to_return:
                return word
    return None


def get_char_numbers_to_reveal(
    amount_chars_to_reveal: int,
    length_word_to_guess: int
) -> list[int]:
    ''''''
    result = []
    i = 0

    while i < amount_chars_to_reveal:
        next_number_to_reveal = random.randint(0, length_word_to_guess-1)
        if next_number_to_reveal in result:
            continue
        result.append(next_number_to_reveal)
        i += 1
        
    return result


def hide_some_word_chars(word_to_guess: str) -> list[str]:
    original_chars = list(word_to_guess)
    revealed_chars = ['*'] * len(word_to_guess)

    chars_numbers_to_reveal = get_char_numbers_to_reveal(
        amount_chars_to_reveal=(len(word_to_guess) + 1) // 5 + 1,
        length_word_to_guess=len(word_to_guess)
    )

    for i in chars_numbers_to_reveal:
        revealed_chars[i] = original_chars[i]

    return revealed_chars


def init_game_state(word_to_guess: str) -> dict:
    return {
        'original_word_chars': list(word_to_guess),
        'revealed_word_chars': hide_some_word_chars(word_to_guess),
        'max_attempts': 6,
        'player_attempts_done': 0
    }


def is_letter_already_guessed(letter: str, game_state: dict) -> bool:
    return letter in game_state['original_word_chars'] \
        and \
        game_state['revealed_word_chars'].count(letter) \
        == game_state['original_word_chars'].count(letter)


def is_new_letter_guessed(letter: str, game_state: dict) -> bool:
    return letter in game_state['original_word_chars'] \
        and \
        game_state['revealed_word_chars'].count(letter) \
        != game_state['original_word_chars'].count(letter)


def reveal_char(letter: str, game_state: dict) -> None:
    for i, val in enumerate(game_state['original_word_chars']):
        if val == letter:
            game_state['revealed_word_chars'][i] = letter


def process_move(letter: str, game_state: dict) -> tuple[int, str]:
    if is_letter_already_guessed(letter, game_state):
        return (-1, f'Символ {letter} уже открыт.')

    if is_new_letter_guessed(letter, game_state):
        reveal_char(letter, game_state)
        return (0, f'Открыт символ {letter}. Поздравляем!')

    game_state['player_attempts_done'] += 1

    return (0, f'Символ {letter} отсутствует в слове.')


def is_end_of_game(game_state: dict) -> bool:
    return game_state['player_attempts_done'] >= game_state['max_attempts'] \
        or '*' not in game_state['revealed_word_chars']


def is_win(game_state: dict) -> bool:
    return '*' not in game_state['revealed_word_chars']

if __name__ == '__main__':
    words = [
        [1, 'абажур'], [2, 'авангард'], [3, 'аванпост'],
        [4, 'адвокат'], [5, 'академик'], [6, 'бабочка'],
        [7, 'бегемот'], [8, 'библиотека'], [9, 'биатлон'],
        [10, 'благо'], [11, 'вагонетка'], [12, 'вегетарианец'],
        [13, 'ведомость'], [14, 'вёрстка'], [15, 'взаимодействие'],
        [16, 'гавань'], [17, 'гвоздика'], [18, 'гобелен'],
        [19, 'губернатор'], [20, 'гнездо'], [21, 'давление'],
        [22, 'двигатель'], [23, 'деавтоматизация'], [24, 'джентльмен'],
        [25, 'дзюдоист'], [26, 'жаворонок'], [27, 'жонглирование'],
        [28, 'жульничество'], [29, 'жемчужина'], [30, 'жонглёр'],
        [31, 'завтрак'], [32, 'запонки'], [33, 'зефир'],
        [34, 'импровизация'], [35, 'иллюминация']
    ]

    test_number = 1  # Choose test number.

    if test_number == 0:  # get_random_word
        print('TEST get_random_word')
        for i in range(10):
            print(i, get_random_word('data/test_words.csv'))
    elif test_number == 1:  # hide_word_chars
        print('TEST hide_word_chars')
        for i, word in words:
            print(f'{list(word)}')
            print(f'{hide_some_word_chars(word)}')
            if (i % 5) == 0:
                print()
    elif test_number == 2:  # init_game_state
        print('TEST init_game_state')
        game_state = init_game_state('бегемот')
        print(f'{game_state["original_word_chars"]=}')
        print(f'{game_state["revealed_word_chars"]=}')
        print(f'{game_state["max_attempts"]=}')
        print(f'{game_state["player_attempts_done"]=}')
    elif test_number == 3:  # process_move
        print('TEST process_move')
        word_to_guess = 'бегемот'
        game_state = {
            'original_word_chars': ['б', 'е', 'г', 'е', 'м', 'о', 'т'],
            # Получить слово со скрытыми симоволами
            'revealed_word_chars': ['б', '*', '*', '*', '*', '*', 'т'],
            'max_attempts': 6,
            'player_attempts_done': 0,
            'is_win': None,
            'is_lose': None
        }

        print(
            f'{process_move("е", game_state), game_state['revealed_word_chars']}')
        print(
            f'{process_move("е", game_state), game_state['revealed_word_chars']}')
        print(
            f'{process_move("м", game_state), game_state['revealed_word_chars']}')
        print(
            f'{process_move("о", game_state), game_state['revealed_word_chars']}')
        print(
            f'{process_move("г", game_state), game_state['revealed_word_chars']}')

        print()

        game_state = {
            'original_word_chars': ['б', 'е', 'г', 'е', 'м', 'о', 'т'],
            # Получить слово со скрытыми симоволами
            'revealed_word_chars': ['*', 'е', '*', '*', '*', '*', 'т'],
            'max_attempts': 6,
            'player_attempts_done': 0,
            'is_win': None,
            'is_lose': None
        }

        print(
            f'{process_move("ю", game_state), game_state['revealed_word_chars']}')
        print(
            f'{process_move("ю", game_state), game_state['revealed_word_chars']}')
        print(
            f'{process_move("ю", game_state), game_state['revealed_word_chars']}')
        print(
            f'{process_move("ю", game_state), game_state['revealed_word_chars']}')
        print(
            f'{process_move("ю", game_state), game_state['revealed_word_chars']}')
        print(
            f'{process_move("ю", game_state), game_state['revealed_word_chars']}')
    elif test_number == 4:  # is_end_of_game
        game_state = {
            'original_word_chars': ['б', 'е', 'г', 'е', 'м', 'о', 'т'],
            # Получить слово со скрытыми симоволами
            'revealed_word_chars': ['б', 'е', 'г', 'е', 'м', 'о', 'т'],
            'max_attempts': 6,
            'player_attempts_done': 5,
            'is_win': None,
            'is_lose': None
        }
        print(f'{is_end_of_game(game_state)=}')
        assert is_end_of_game(game_state) == True

        game_state = {
            'original_word_chars': ['б', 'е', 'г', 'е', 'м', 'о', 'т'],
            # Получить слово со скрытыми симоволами
            'revealed_word_chars': ['б', 'е', 'г', 'е', 'м', '*', 'т'],
            'max_attempts': 6,
            'player_attempts_done': 6,
            'is_win': None,
            'is_lose': None
        }
        print(f'{is_end_of_game(game_state)=}')
        assert is_end_of_game(game_state) == True

        game_state = {
            'original_word_chars': ['б', 'е', 'г', 'е', 'м', 'о', 'т'],
            # Получить слово со скрытыми симоволами
            'revealed_word_chars': ['б', 'е', 'г', 'е', 'м', '*', 'т'],
            'max_attempts': 6,
            'player_attempts_done': 0,
            'is_win': None,
            'is_lose': None
        }
        print(f'{is_end_of_game(game_state)=}')
        assert is_end_of_game(game_state) == False
