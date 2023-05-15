import random
def find_percentage_shipdestroyed_and_winner():
    p1=P1/20*100
    p2=P2/20*100
    print('percentage of player1 ship destroyed is',p1)
    print('percentage of player2 ship destroyed is',p2)
    if p1 > p2:
        print('opponent wins')
    elif p2 > p1:
        print('you  wins')
    else:
        print('you went draw')
def create_ships():
    ships_player=[]
    for i in range(20):
        ship=(random.randint(0,10-1),random.randint(0,10-1))
        ships_player.append(ship)
    return(ships_player)
