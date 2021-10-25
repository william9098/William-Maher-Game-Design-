#william maher
#10/25/21 Learning Fonts and Blit

import pygame, os, random, time

from pygame.display import update


pygame.init()
BLACK=(0,0,0)
WHITE=(255,255,255)
WIDTH=800
HEIGHT=800
window=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Setting Window")

#TITLE_FONT=pygame.font.SysFont(name, size, bold=False, italic=False)
TITLE_FONT=pygame.font.SysFont('comicsans', 80)
SubTitle=pygame.font.SysFont('comicsans', 40, italic=True)
def display_message(message):
    pygame.time.delay(100)
    text= TITLE_FONT.render(message, 1, WHITE) #render prints text
   # window.blit(text, (WIDTH/2-text.get_width()/2), (HEIGHT/2-text.get_height()/2))
    window.blit(text, (WIDTH/2-text.get_width()/2, 70))
    pygame.display.update()
    pygame.time.delay(100)



run=True 
while run:
    for eve in pygame.event.get():
        if eve.type == pygame.QUIT: #pygame.QUIT is looking for a key pressed, while pygame.quit() is a function
            run=False
            pygame.quit()
    window.fill((0,0,0))
    display_message("SETTINGS")
    pygame.time.delay(300)

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
pygame.quit()