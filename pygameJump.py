import os
import pygame as py
from pygame import event
from pygame.constants import K_SPACE
WIDTH=800
HEIGHT=800


boulder=py.Rect(WIDTH-300, HEIGHT-200, 100, 200)

#first thing
py.init()
 
#create window
height= 700
width = 800
colors = {'red':(150,0,0),'green':(0,200,0), 'blue':(0,0,255), 'purple':(150, 0, 150), 'white':(255,255,255), 'black':(0,0,0) }
screen=py.display.set_mode((width, height))
myColor= colors.get('purple')
screen.fill(myColor)
py.display.set_caption("Moving Square")
py.display.flip()
#parameters to define our square
x=width/2
y=height/2
wbox=50
hbox=50
#creating out object square
square=py.Rect(x,y,wbox, hbox )
#draw object
objColor=colors.get('red')
boulderColor=colors.get('blue')
py.draw.rect(screen, objColor, square)
py.draw.rect(screen, boulderColor, boulder)
py.display.update()
#create speed to move the object on the screen
speed = 10
run=True #Variable to control the main loop
#boolean to check for jump
move=True
Jumping=False
jumpCount=10
while run:

    py.time.delay(100) #milliseconds
    for anyThing in py.event.get():
        if anyThing.type == py.QUIT:
            run =False
    keyPressed= py.key.get_pressed()
    # if square.y <HEIGHT-200-hbox:
    if keyPressed[py.K_RIGHT] and square.x <WIDTH-wbox-speed and move:
        if square.colliderect(boulder):
            square.x-=5
        else:
            square.x += speed
    if keyPressed[py.K_LEFT] and square.x>speed:
            square.x -= speed
    
    elif square.x <=boulder.x-wbox-5:
        if keyPressed[py.K_RIGHT]:
            square.x+=speed
    

       
    if not(Jumping):
        if keyPressed[py.K_DOWN] and square.y >speed:
            square.y += speed
        if keyPressed[py.K_UP] and square.x>speed:
            #if square.collidepoint(boulder.x,boulder.y):
            square.y -= 5
        if keyPressed[py.K_SPACE]:
            Jumping=True
    else:
        if jumpCount >=-10:
            square.y -= jumpCount*abs(jumpCount)**0.5
            jumpCount-=1
        else:
            jumpCount=10
            Jumping=False
    # if(py.Rect.collidepoint(boulder, (square.x+wbox/2, square.y))):
    #     move=False
    #     square.x=square.x-wbox
    #     move=True



    screen.fill(myColor)
    py.draw.rect(screen, objColor, square)
    py.draw.rect(screen, boulderColor, boulder)
    py.display.flip()
py.quit()


#for pictures, 64 x 64, get find a picture with no background
#500-525, 600