from random import shuffle
color_list = ['RED', 'BLUE', 'YELLOW', 'GREEN']


#r A
def draw_card(DECK, player_, DISCARD, PLAYER_LIST):
    def deck_renew(DISCARD):
        # new discard is the last card played
        new_discard = [DISCARD.pop(-1)]
        deck = []

        # add cards from discard back into deck
        # reset colors of special cards to black
        for card_ in DISCARD:
            if card_.number != 'CC':
                if card_.number != '+4':
                    deck.append(card_)
            else:
                card_.color = 'BLACK'
                card_.display = card_.number + ' ' + card_.color[0]
                card_.colored_display = colored(220,220,220, card_.display)
                deck.append(card_)

        # shuffle deck; return the deck and the new discard pile
        shuffle(deck)
        return deck, new_discard

    # check to see if there is card to draw
    if len(DECK)==0:
        DECK, DISCARD = deck_renew(DISCARD)

    # draw card
    player_.hand.append(DECK.pop(0))

    #user notification
    if player_.name == 'USER':
        print('\nYou drew a card!')
    # return any new values
    PLAYER_LIST = refresh_player_list(player_, PLAYER_LIST)
    return DECK, player_, DISCARD, PLAYER_LIST

#r player.hand
def sort_player_hand(player_hand):
    player_hand.sort(key=lambda card: card.sort_value)
    return player_hand

#r A
def player_turn_init(DECK, player_, DISCARD, PLAYER_LIST):
# check if there is a valid move, if not draw until there is.

    # checking for viable moves
    possible_move = False
    for card_ in player_.hand:
        if card_.color == 'BLACK':
            possible_move = True
            break
        if card_.number == DISCARD[-1].number:
            possible_move = True
            break
        if card_.color == DISCARD[-1].color:
            possible_move = True
            break

    # while there are no viable moves
    while possible_move == False:

            # draw a card
            DECK, player_, DISCARD, PLAYER_LIST = draw_card(DECK, player_, DISCARD, PLAYER_LIST)

            # check new card to see if it is viable
            if player_.hand[-1].color == 'BLACK':
                possible_move = True
            if player_.hand[-1].number == DISCARD[-1].number:
                possible_move = True
            if player_.hand[-1].color == DISCARD[-1].color:
                possible_move = True

    # sort player hand; update values
    if player_.name=='USER':
        player_.hand = sort_player_hand(player_.hand)

    # if there is a valid move and current player has 2 cards, announce uno!
    if len(player_.hand) == 2:
        print('\n!UNO!\n')
        if player_.name=='USER':
            print('(After this move you will only have one card!)')
    return DECK, player_, DISCARD, PLAYER_LIST

#r List of turn order from current player
def turn_order_definer(player_, PLAYER_LIST):
    current_player=player_
    old_dict = {v: i for i, v in enumerate(PLAYER_LIST)}
    new_dict = {}
    sort_list=[]
    for i, (tuple1, tuple2) in enumerate(old_dict.items()):
        key, value = tuple1, tuple2
        if value < old_dict[current_player]:
            new_dict[value + 4] = key
            sort_list.append(value+4)
        else:
            new_dict[value]=key
            sort_list.append(value)
    sort_list.sort()
    answer=[new_dict[sort_list[index]] for index in range(len(sort_list)) if new_dict[sort_list[index]]!=current_player]
    return answer
'''
    plalist = starting_deck.gen_players()
    pla=plalist[randint(0,3)]
    
    x=turn_order_definer(pla, plalist)
    x_na= [i.name for i in x]
    plalist.reverse()
    y=turn_order_definer(pla, plalist)
    y_na= [i.name for i in y]
    
    print(x)
    print(y)
    print(x_na)
    print(y_na)
    '''

# r Color, choice if ai plays black
def ai_choice_black(player_):

    #Make a color counter
    color_count = {k: 0 for k in color_list}
    for card_ in player_.hand:
        if card_.color!='BLACK':
            color_count[card_.color] += 1

    #Find color with most cards in hand
    biggest = max([i for i in color_count.values()])

    #Return
    for elem in color_list:
        if color_count[elem] == biggest:
            return elem


    #answer = count_color[sort_list[-1]]
    #print(answer)
    #return answer

# r Color, userinput if user plays black
def user_choice_black():
    # definitions
    first_let=[i[0] for i in color_list]
    # check to see if input is only one letter and if so to correct to the appropriate color
    def first_let_check(input_):
        if input_ in first_let:
            index_ = first_let.index(input_)  #index fx returns first index value
            input_ = color_list[index_]
        return input_

    # input
    user_choice = input('You played a black card, please choose your desired color: ')
    user_choice = user_choice.upper()

    # first letter checker
    user_choice = first_let_check(user_choice)

    # if invalid input
    while user_choice not in color_list:

        # input again
        user_choice = input('Invalid input, please type the color again: ')
        user_choice = user_choice.upper()

        # first letter checker
        user_choice = first_let_check(user_choice)

    return user_choice

# Redundant Fx
# from sys import exit
# from time import sleep
# def victory(player_):
#     if len(player_.hand) == '0':
#         print(f'PLAYER {player_.name} WINS!!!!!!!!!!!!!!!!!')
#         print('Open or restart program to play again.')
#         sleep(10)
#         exit(0)

# r turn_counter
def game_state_check(player_, PLAYER_LIST, skip):

    turn_counter = PLAYER_LIST.index(player_)

    turn_counter+=1
    if turn_counter >= 4:
        turn_counter = turn_counter % 4

    if skip is True:

        if PLAYER_LIST[turn_counter].name=='USER':
            print('\nYou have been skipped!\n')
        else:
            print(f'{PLAYER_LIST[turn_counter].name} has been skipped')

        turn_counter+=1
        if turn_counter >= 4:
            turn_counter = turn_counter % 4

    return turn_counter

# r PLAYER_LIST
def refresh_player_list(player_, PLAYER_LIST):
    for i, elem in enumerate(PLAYER_LIST):
        if elem.name==player_.name:
            PLAYER_LIST[i]=player_
    return PLAYER_LIST

def colored(r, g, b, text):
    return "\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(r, g, b, text)


RGB_dict = {'RED': [255, 0, 0], 'BLUE': [50, 150, 255], 'YELLOW': [250, 250, 0], 'GREEN': [20, 255, 20]}

# USEFUL TIP
# select multiple lines then click (ctrl+/) to comment them all out at the same time

# list.counter(value) returns number of instances of said value in list






