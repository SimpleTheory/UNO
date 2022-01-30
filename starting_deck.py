# DEFINITIONS
from random import shuffle
class player:
    def __init__(self, name, hand):
        self.name = name
        self.hand = hand
class card:
    def __init__(self, number, color):
        self.number = number
        self.color = color

    # display
        if isinstance(number, int):
            self.display = str(number)+color[0]
        if isinstance(number, str):
            self.display = number+' '+color[0]

    # sort value
        if number=='+4':
            sort_val=13
        elif isinstance(number, str):
            sort_val=len(number)+10
        else:
            sort_val=number
        color_list = ['RED', 'BLUE', 'YELLOW', 'GREEN', 'BLACK']

        self.sort_value = ((color_list.index(color)+1)*100)+sort_val



# FUNCTIONS
def gen_players():
    USER = player('USER', [])
    AI_1 = player('AI 1', [])
    AI_2 = player('AI 2', [])
    AI_3 = player('AI 3', [])
    PLAYER_LIST = [USER, AI_1, AI_2, AI_3]
    shuffle(PLAYER_LIST)
    return PLAYER_LIST


def deck_gen():
    color_list = ['RED', 'BLUE', 'YELLOW', 'GREEN']
    STARTING_DECK=[]
    for elem in color_list:
        for i in range(0,10):
            STARTING_DECK.append(card(i, elem))
            STARTING_DECK.append(card(i, elem))

        for i in range(2):
            STARTING_DECK.append(card('+2', elem))
            STARTING_DECK.append(card('SKIP', elem))
            STARTING_DECK.append(card('REVERSE', elem))

    for i in range(4):
        STARTING_DECK.append(card('+4', 'BLACK'))
        STARTING_DECK.append(card('CC', 'BLACK'))
    #x=[i.display for i in STARTING_DECK]
    #print(x)
    shuffle(STARTING_DECK)
    return STARTING_DECK

#r A
def game_init():
    # gen players, deck, discard pile
    PLAYER_LIST = gen_players()
    DECK = deck_gen()
    
    #DISCARD = [DECK.pop(0)]
    # if card black skip, else put card into play
    for i, v in enumerate(DECK):
        if v.color == 'BLACK':
            continue
        else:
            DISCARD = [DECK.pop(i)]
            break

    # for every player draw 7 cards
    for player_ in PLAYER_LIST:
        for i in range(7):
            player_.hand.append(DECK.pop(0))

    return DECK, PLAYER_LIST, DISCARD








