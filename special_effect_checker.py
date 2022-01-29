import subroutine
#r card_to_play | PLAYER_LIST | some sort of move counter
def special_effect_check(card_to_play, DECK, player_, DISCARD, PLAYER_LIST):

    #DEFINITIONS:
    turn_order = subroutine.turn_order_definer(player_,  PLAYER_LIST)
    next_guy = turn_order[0]
    skip=False

    #r card_to_play
    def black(player_, active_card):
        if player_.name=='USER':
            color_ = subroutine.user_choice_black()
        else:
            color_ = subroutine.ai_choice_black(player_)
        active_card.color = color_
        active_card.display = active_card.number + ' ' + active_card.color
        return active_card


    #THE LIST OF EFFECTS:

    if card_to_play.number=='+4':
        for i in range(4):
            DECK, next_guy, DISCARD, PLAYER_LIST = subroutine.draw_card(DECK, next_guy, DISCARD, PLAYER_LIST)
        card_to_play=black(player_, card_to_play)
        skip=True

    if card_to_play.number == 'CC':
        card_to_play = black(player_, card_to_play)

    if card_to_play.number == 'REVERSE':
        PLAYER_LIST.reverse()
        #print(f'{player_.name} has REVERSED!')

    if card_to_play.number == 'SKIP':
        skip=True

    if card_to_play.number == '+2':
        for i in range(2):
            DECK, next_guy, DISCARD, PLAYER_LIST = subroutine.draw_card(DECK, next_guy, DISCARD, PLAYER_LIST)
        skip=True

    return card_to_play, DECK, DISCARD, PLAYER_LIST, skip
