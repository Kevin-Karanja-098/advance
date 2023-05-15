def fightzone():
    global board
    board = [[0]*10 for i in range(10)]
    return board
def display_gamekey():
    print('key')
    print('W=when you hit target')
    print('L=when you misses target')
    print('G=when opponent hit target')
    print('F=when opponent misses target')
