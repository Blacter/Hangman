import re


def is_game_start() -> bool:
    user_choice = input()
    if len(user_choice) == 0:
        raise ValueError('Incorrect input: input should not be empty')
    elif not re.search('^[YyNn]$', user_choice):
        raise ValueError('Incorrect input: choice should be Y or N')    
    
    user_choice = user_choice.lower()
    if user_choice == 'y':
        return True
    else:
        return False
    
    
def get_user_choice() -> bool:
    is_input_correct = False
    while not is_input_correct:
        try:
            user_choice = is_game_start()
        except ValueError as e:
            print(e)
        else:
            is_input_correct = True
    
    return user_choice


def input_assumed_letter() -> 'str':
    assumed_letter = input('> ')
    if not re.search('^[А-Яа-яё]$', assumed_letter):
        raise ValueError('Inputed value should be russian letter')        
    else:
        return assumed_letter.lower()
        

def get_assumed_letter() -> str:
    is_input_correct = False
    while not is_input_correct:
        try:
            assumed_letter = input_assumed_letter()
        except ValueError as e:
            print(e)
        else:
            is_input_correct = True
    return assumed_letter