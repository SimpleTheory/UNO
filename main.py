#IMPORTS
import starting_deck
import turn_operation
import subroutine
from sys import exit
from time import sleep
#CLASS DEF
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

#DEFINITIONS
#DECK, PLAYER_LIST, DISCARD = starting_deck.game_init()
#turn_counter=0


#MAIN
def MAIN():

    # DEFINITIONS
    DECK, PLAYER_LIST, DISCARD = starting_deck.game_init()
    turn_counter = 0
    space='\n'*2
    won= False

    print('''
INDEX:
    CC = Change color
    Cards attributed with number then color (ie 4R or SKIP G)
!LET'S PLAY UNO!
    ''')

    # LOOP
    while won==False:

        # UPKEEP
        current_player = PLAYER_LIST[turn_counter]
        if current_player.name=='USER':
            print(space)


        # MAIN PHASE
        if current_player.name=='USER':
            DECK, DISCARD, PLAYER_LIST, skip = turn_operation.user_turn(DECK, current_player, DISCARD, PLAYER_LIST)
        else:
            DECK, DISCARD, PLAYER_LIST, skip = turn_operation.ai_turn(DECK, current_player, DISCARD, PLAYER_LIST)


        # END PHASE
        x = [i for i in PLAYER_LIST if i.name == current_player.name]
        y = x[0]
        if len(y.hand)==0:
            won=True

        if current_player.name=='USER':
            print(space)
            
        turn_counter = subroutine.game_state_check(current_player, PLAYER_LIST, skip)

    #Post loop victory messages
    x = [i.name for i in PLAYER_LIST if len(i.hand) == 0]
    y = x[0]
    print(f'PLAYER {y} WINS!!!!!!!!!!!!!!!!!')
    print('Open or restart program to play again.')
    sleep(10)
    exit(0)
'''
current_player=PLAYER_LIST[turn_counter]
turn operation
game state check
'''




if __name__ == '__main__':
    MAIN()


#build main loop
#go through everything make sure all ok
#run program make sure all ok
