import random
def opponent_shoot():
    global x
    global y
    x=random.randint(0,10-1)
    y=random.randint(0,10-1)
    global shoot
    shoot=(x,y)
    return shoot
