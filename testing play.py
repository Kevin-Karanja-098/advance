import pygame
pygame.init() 
width=500
height=500
scr=pygame.display.set_mode([width,height])
pygame.display.set_caption('karanja try to learn')
positionx=250
positiony=250
movex=1
movey=1
def move_object_to_right():
    global positionx
    global movex
    if positionx<500:
            positionx+=movex
            
def move_object_to_down():
    global positiony
    global movey
    if positiony<500:
            positiony+=movey
def move_object_to_left():
    global positionx
    global movex
    if positionx<=500:
            positionx-=movex
def move_object_to_up():
    global positiony
    global movey
    if positiony<=500:
            positiony-=movey
looping=True
while looping:
    pygame.time.delay(6)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            looping=False
    if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and positionx>0:
                    move_object_to_left()
                elif event.key == pygame.K_RIGHT and positionx<450:
                    move_object_to_right()
                elif event.key == pygame.K_UP and positiony>0:
                    move_object_to_up()
                elif event.key == pygame.K_DOWN and positiony<450:
                    move_object_to_down()
##    scr.fill((0,0,25))
    pygame.draw.rect(scr,(0,0,200),(positionx,positiony,50,50))
    pygame.display.flip()
pygame.quit()
    
