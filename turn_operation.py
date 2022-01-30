import subroutine
from special_effect_checker import special_effect_check
from random import choice
acc_colors = {'R': 'RED', 'G': 'GREEN', 'Y': 'YELLOW', 'B': 'BLUE'}

def move_validator_user(selection, player_, DISCARD):
    # gen possible move and a list of card displays to use to check if sel in player hand
    possible_move = False

    # if user inputted something retarded
    if selection == 'PPPP':
        return possible_move

    # if selection is in the player's hand
    keys = [i.display for i in player_.hand]
    if selection in keys:

        # identify card object equivalent of selection
        index_ = keys.index(selection)
        selection=player_.hand[index_]

        # check to see if the move is valid
        if selection.color == 'BLACK':
            possible_move = True
        elif selection.number == DISCARD[-1].number:
            possible_move = True
        elif selection.color == DISCARD[-1].color:
            possible_move = True
        else:
            possible_move = False

    return possible_move


def move_validator_ai(selection, DISCARD):
    # check to see if the move is valid
    if selection.color == 'BLACK':
        possible_move = True
    elif selection.number == DISCARD[-1].number:
        possible_move = True
    elif selection.color == DISCARD[-1].color:
        possible_move = True
    else:
        possible_move = False


    if possible_move == True:
        return selection
    else:
        return possible_move

#FOR USER
def input_formatter(string):
    string = string.upper()
    final_out = 'PPPP'

    # if regular card
    temp_digit = [i.isdigit() for i in string]
    if True in temp_digit:
        if '+' not in string:
            temp = set(string)
            temp = list(temp)

            nums = [i for i in temp if i.isdigit() == True]
            let = [i for i in temp if i.isalpha() == True]

            nums.extend(let)
            final_out = ''.join(nums)
            return final_out

    # if special card

    black = ['+4', 'CC']
    acceptable = ['+2', 'REVERSE', 'SKIP']


    # if black
    for elem in black:
        if elem in string:
            final_out = f'{elem} B'

    # if other correct value
    for elem in acceptable:
        if elem in string:
            temp=string.replace(elem, '')
            color_keys=acc_colors.keys()
            for i in range(len(temp)):
                if temp[i] in color_keys:
                    final_out = f'{elem} {temp[i]}'

    return final_out

# r DECK, DISCARD, PLAYER_LIST, skip
def user_turn(DECK, player_, DISCARD, PLAYER_LIST):

    # turn initiation
    DECK, player_, DISCARD, PLAYER_LIST = subroutine.player_turn_init(DECK, player_, DISCARD, PLAYER_LIST)
    turn_order_list= subroutine.turn_order_definer(player_, PLAYER_LIST)

    # print ui
    print('\nThe following are the other players and their hands, in order of who\'s going next:')
    for element in turn_order_list:
            print(f'    {element.name} has {len(element.hand)}')
    print(f'\nCard to play off of: {DISCARD[-1].colored_display}')
    print(f'\nYour Hand: {len(player_.hand)}')

    # print colored lists of player hand
    colored_display_list = [i.colored_display for i in player_.hand]
    print('(', end='')
    for i, v in enumerate(colored_display_list):
        if i == len(colored_display_list) - 1:
            print(v, end=')\n')
        else:
            print(v, end=', ')

    # print possible moves
    x = [move_validator_ai(card, DISCARD) for card in player_.hand]
    possible_display=[i.colored_display for i in x if i is not False]
    print('\n(Possible moves: ( ', end='')
    for i, v in enumerate(possible_display):
        if i == len(possible_display) - 1:
            print(v, end='))\n')
        else:
            print(v, end=', ')

    # player input and verification
    u_input= input_formatter(input('\nType in the card you wish to play (beware of typos):\n'))
    valid=move_validator_user(u_input, player_, DISCARD)
    while valid==False:
        print('Invalid Move')
        u_input = input_formatter(input('Please input another move (hopefully a valid one):\n '))
        valid = move_validator_user(u_input, player_, DISCARD)

    # actuating
    keys = [i.display for i in player_.hand]
    index_ = keys.index(u_input)
    card_to_play = player_.hand.pop(index_)
    card_to_play, DECK, DISCARD, PLAYER_LIST, skip = special_effect_check(card_to_play, DECK, player_, DISCARD, PLAYER_LIST)
    DISCARD.append(card_to_play)

    # return relevant values
    return DECK, DISCARD, PLAYER_LIST, skip


#FOR AI

# r DECK, DISCARD, PLAYER_LIST, skip
def ai_play_card(fitted_possibilities, DECK, player_, DISCARD, PLAYER_LIST):
    if len(fitted_possibilities)>1:
        selection = choice(fitted_possibilities)
    else:
        selection = fitted_possibilities[0]
    index_= player_.hand.index(selection)
    card_to_play=player_.hand.pop(index_)
    card_to_play, DECK, DISCARD, PLAYER_LIST, skip = special_effect_check(card_to_play, DECK, player_, DISCARD, PLAYER_LIST)
    print(f'{player_.name} played the card {card_to_play.colored_display}.')
    DISCARD.append(card_to_play)
    return DECK, DISCARD, PLAYER_LIST, skip
'''
    know what possible moves there are 

    if next player has 1 card
        if draw card 
            play
        elif reverse or skip play


    if draw cards are available
        if next player has 3 or less cards
            play

    if there are non-black duplicate cards
        play one of duplicates

    elif if there are non-black options
        play a random one

    else:
        play opt



    '''

#r fitted opt list for AI
def ai_ai(next_guy, possible):

    non_black_int_options = [i for i in possible if i.color != 'BLACK' and i.number is int]
    num_dup = [i.number for i in possible]
    possible_duplicates = [card_ for index, card_ in enumerate(possible) if num_dup.count(num_dup[index]) > 1]

    if len(next_guy.hand) == 1:
        fitted = [card_ for card_ in possible if card_.number is str and '+' in card_.number]
        if len(fitted) == 0:
            fitted = [card_ for card_ in possible if card_.number is str]
            if len(fitted) > 0:
                return fitted

    if len(next_guy.hand) < 4:
        fitted = [card_ for card_ in possible if card_.number is str and card_.color != 'BLACK']
        fitted.extend(non_black_int_options)
        if len(fitted) > 0:
            return fitted
        else:
            return possible

    elif len(possible_duplicates) > 0:
        return possible_duplicates

    else:
        if len(non_black_int_options) > 0:
            return non_black_int_options
        elif len([i for i in possible if i.color != 'BLACK']) > 0: #non black options in general
            return [i for i in possible if i.color != 'BLACK']
        else:
            return possible

#r DECK, DISCARD, PLAYER_LIST, skip
def ai_turn (DECK, player_, DISCARD, PLAYER_LIST):
    # turn init
    DECK, player_, DISCARD, PLAYER_LIST = subroutine.player_turn_init(DECK, player_, DISCARD, PLAYER_LIST)
        # definitions
    x = [move_validator_ai(card, DISCARD) for card in player_.hand]
    possible=[i for i in x if i is not False]
    turn_order = subroutine.turn_order_definer(player_, PLAYER_LIST)
    next_guy = turn_order[0]

    # selection
    fitted_selection = ai_ai(next_guy, possible)

    # actuation and returns
    DECK, DISCARD, PLAYER_LIST, skip = ai_play_card(fitted_selection, DECK, player_, DISCARD, PLAYER_LIST)
    return DECK, DISCARD, PLAYER_LIST, skip
