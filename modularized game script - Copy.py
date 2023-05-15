import random
import time
from package3.package2.package1 import display_fight as ds,prepare_fight as pf
from package3.package2 import attacking as att
from package3 import opponent_attack as opp
P1=0
P2=0
time_limit=300
start_time=time.time()
board=ds.fightzone()
ships_player1=pf.create_ships()
ships_player2=pf.create_ships()
ds.display_gamekey()
while True:
    print('your turn')
    print('enter coordinates to shoot')
    x=int(input())
    y=int(input())
    fire=(x,y)
    if fire in ships_player2:
        board[x][y]='W'
        P1+=1
    else:
        board[x][y]='L'
    for i in board:
         print(*i)
    if time.time() -start_time  > time_limit:
        print("TIME'S UP")
        print('GAME OVER')
        break
    print("opponent's turn")
    time.sleep(2)
    x=random.randint(0,10-1)
    y=random.randint(0,10-1)
    shoot=(x,y)
    if shoot in ships_player1:
        board[x][y]='G'
        P2+=1
    else:
        board[x][y]='F'
    for i in board:
         print(*i)
    if time.time() -start_time  > time_limit:
        print("TIME'S UP")
        print('GAME OVER')
        break
pf.find_percentage_shipdestroyed_and_winner()
