def you_shoot():
    print('your turn')
    print('enter coordinates to shoot')
    global x
    global y
    x=int(input())
    y=int(input())
    global fire
    fire=(x,y)
    return fire
