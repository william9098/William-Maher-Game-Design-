#william maher
#10/25/21 Learning Fonts and Blit

import pygame as py, os, random, time




py.init()
BLACK=(0,0,0)
WHITE=(255,255,255)
WIDTH=800
HEIGHT=800
window=py.display.set_mode((WIDTH,HEIGHT))
py.display.set_caption("Setting Window")

#TITLE_FONT=pygame.font.SysFont(name, size, bold=False, italic=False)
TITLE_FONT=py.font.SysFont('comicsans', 80)
SubTitle=py.font.SysFont('comicsans', 40, italic=True)

def display_message(message):
    #py.time.delay(100)
    text= TITLE_FONT.render(message, 1, WHITE) #render prints text
   # window.blit(text, (WIDTH/2-text.get_width()/2), (HEIGHT/2-text.get_height()/2))
    window.blit(text, (WIDTH/2-text.get_width()/2, 10))
    py.display.update()
    py.time.delay(100)
    

def display_message2(message):
    py.time.delay(100)
    text= TITLE_FONT.render(message, 2, WHITE) #render prints text
   # window.blit(text, (WIDTH/2-text.get_width()/2), (HEIGHT/2-text.get_height()/2))
    window.blit(text, (WIDTH/2-text.get_width()/2, 70))
    py.display.update()
    #py.time.delay(100)

def display_message3(message):
    #py.time.delay(100)
    text= TITLE_FONT.render(message, 3, WHITE) 
    window.blit(text, (WIDTH/2-text.get_width()/2, 130))
    py.display.update()
    #py.time.delay(100)

def display_message4(message):
    #py.time.delay(100)
    text= TITLE_FONT.render(message, 4, WHITE) 
    window.blit(text, (WIDTH/2-text.get_width()/2, 200))
    py.display.update()
    #py.time.delay(100)



run=True 
while run:
    for eve in py.event.get():
        if eve.type == py.QUIT: #pygame.QUIT is looking for a key pressed, while pygame.quit() is a function
            run=False
            py.quit()
        window.fill((0,0,0))
    display_message("SETTINGS")
    display_message2("Background Color")
    display_message3("Object Color")
    display_message4("Sound=On/Off")
    #py.time.delay(300)
    py.display.update()


#print the rest of your menu for settings
# 
# Windows
# Background Color
# Objet COlors
# Sound= on/off
# for (display_message (x,y)) 
#for (i in range)


# display_message("oops")
#     pygame.time.delay(300)
#     window.fill(BLACK)
#     display_message("AHHHH")
#     pygame.time.delay(300)
#     window.fill(BLACK)
