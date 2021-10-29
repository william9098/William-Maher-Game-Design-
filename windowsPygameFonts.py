#william maher
#10/25/21 Learning Fonts and Blit

import pygame as py, os, random, time

DISPLAY_MAIN_MENU=0
DISPLAY_INSTRUCTIONS=1
DISPLAY_LEVEL1=2
DISPLAY_LEVEL2=3
DISPLAY_SETTINGS=4
DISPLAY_SCOREBOARD=5
DISPLAY_SETTINGS_BACKGROUND_COLOR=6
DISPLAY_SETTINGS_OBJECT_COLOR=7
DISPLAY_SETTINGS_SOUND=8
DISPLAY_SETTINGS_SCREEN_SIZE=9
currentdisplay=DISPLAY_MAIN_MENU


py.init()
BLACK=(0,0,0)
WHITE=(255,255,255)
RED= (150, 0, 0)
MenuMessages=["Instructions", "Level 1", "Level 2", "Settings", "Scoreboard", "Exit"]
settingsmessages=["Background Color", "Object Color", "Sound On/Off", "Screen Size"]

WIDTH=800
HEIGHT=800
window=py.display.set_mode((WIDTH,HEIGHT))
py.display.set_caption("Setting Window")

#TITLE_FONT=pygame.font.SysFont(name, size, bold=False, italic=False)
TITLE_FONT=py.font.SysFont('comicsans', 80)
SubTitle=py.font.SysFont('comicsans', 40, italic=True)
text=TITLE_FONT.render("message", 1, WHITE)
wbox=25
hbox=25
x=70
y=190
square=py.Rect(10,10, wbox, hbox)
#when you want to draw a rectangle you use 'rect' when you want to create a rectangle use 'Rect'

def display_Title(message,y):
    #py.time.delay(100)
    text= TITLE_FONT.render(message, 1, WHITE) #render prints text
    x=WIDTH/2-text.get_width()/2
   # window.blit(text, (WIDTH/2-text.get_width()/2), (HEIGHT/2-text.get_height()/2))
    window.blit(text, (x,y)) #TExt, (x,y)) text, (WIDTH/2-text.get_width()/2, 10
    py.display.update()
    py.time.delay(100)


    

# def display_message2(message):
#     py.time.delay(100)
#     text= SubTitle.render(message, 2, WHITE) #render prints text
#    # window.blit(text, (WIDTH/2-text.get_width()/2), (HEIGHT/2-text.get_height()/2))
#     window.blit(text, (WIDTH/2-text.get_width()/2, 110))
#     py.display.update()
#     #py.time.delay(100)

# def display_message3(message):
#     #py.time.delay(100)
#     text= SubTitle.render(message, 3, WHITE) 
#     window.blit(text, (WIDTH/2-text.get_width()/2, 210))
#     py.display.update()
#     #py.time.delay(100)

# def display_message4(message):
#     #py.time.delay(100)
#     text= SubTitle.render(message, 4, WHITE) 
#     window.blit(text, (WIDTH/2-text.get_width()/2, 310))
#     py.display.update()
#     #py.time.delay(100)

# def display_message5(message):
#     #py.time.delay(100)
#     text= SubTitle.render(message, 5, WHITE) 
#     window.blit(text, (WIDTH/2-text.get_width()/2, 410))
#     py.display.update()
#     #py.time.delay(100)

def display_Menu(messages):
    x=70
    y=190
    square.x=x
    square.y=y
    for i in range(0, len(messages)):
        word=MenuMessages[i]
        py.draw.rect(window, RED, square)
        text=TITLE_FONT.render(word, 1, WHITE)
        window.blit(text, (x+wbox+10,y))
        py.display.flip()
        py.time.delay(100)
        y+=80
        square.y=y

def display_SettingsMenu(messages):
    x=70
    y=190
    square.x=x
    square.y=y
    for i in range(0, len(messages)):
        word=settingsmessages[i]
        py.draw.rect(window, RED, square)
        text=TITLE_FONT.render(word, 1, WHITE)
        window.blit(text, (x+wbox+10,y))
        py.display.flip()
        py.time.delay(100)
        y+=80
        square.y=y



window.fill((BLACK))
display_Title("Main Menu",70)
display_Menu(MenuMessages)
py.display.update()
currentDisplay=DISPLAY_MAIN_MENU
#counter=0
run=True 
while run:
    for eve in py.event.get():
        if eve.type == py.QUIT: #pygame.QUIT is looking for a key pressed, while pygame.quit() is a function
            run=False

        if eve.type==py.MOUSEBUTTONDOWN:
            mouse_pressed=py.mouse.get_pressed()
            if mouse_pressed[0]:
                mouse_pos=py.mouse.get_pos()
                print(py.mouse.get_pos())

            if currentDisplay==DISPLAY_MAIN_MENU:
                if mouse_pos[0]>=70 and mouse_pos[0]<=230 and mouse_pos[1]>=190 and mouse_pos[1]<=210:
                    window.fill(BLACK)
                    display_Title("Instructions", 70)
                    display_Title=("Back", 750)
                    py.display.update()
                    currentDisplay=DISPLAY_INSTRUCTIONS
                    
                if mouse_pos[0]>=75 and mouse_pos[0]<=260 and mouse_pos[1]>=95 and mouse_pos[1]<=300: #71, 193. 93,193. 93, 212. 71, 211
                    window.fill(BLACK)
                    display_Title("Level 1",  70)
                    display_Title=("Back", 750)
                    py.display.update()
                    currentDisplay=DISPLAY_LEVEL1

                if mouse_pos[0]>=70 and mouse_pos[0]<=290 and mouse_pos[1]>=95 and mouse_pos[1]<=400: #71, 193. 93,193. 93, 212. 71, 211
                    window.fill(BLACK)
                    display_Title("Level 2",  70)
                    display_Title("Back", 750)
                    py.display.update()
                    currentDisplay=DISPLAY_LEVEL2
                
                
                if mouse_pos[0] >= 75 and mouse_pos[0] <= 440 and mouse_pos[1]>=90 and mouse_pos[1]<=455:  #75, 435 (top left) 95, 435, (top right) bottom right: 95, 455,  bottom left: 75,
                    window.fill(BLACK)
                    display_Title("Settings",  70)
                    display_SettingsMenu()
                    display_Title("Back", 750)
                    py.display.update()
                    currentDisplay=DISPLAY_SETTINGS
            
            # elif currentDisplay== DISPLAY_MAIN_MENU:   
            #     if mouse_pos[0] >= 390 and mouse_pos[0] <= 335 and mouse_pos[1]>=450 and mouse_pos[1]<=800:
            #         window.fill(BLACK)
            #         display_Title("Main Menu", 20)
            #         display_Menu()
            #         py.display.update()
            #         currentDisplay==DISPLAY_MAIN_MENU
                
py.quit()
        #elif mouse_pos[0] >= 75 and mouse_pos[0] <= 440 and mouse_pos[1]>=90 and mouse_pos[1]<=455:  #75, 435 (top left) 95, 435, (top right) bottom right: 95, 455,  bottom left: 75,
            #run=False
   #338, 755, #461, 765, #464, 794, #338, 792
        




#create main menu with levels with rectangles, settings, instructions, 

#Instructions
# Level 1
# #level 2
#Scoreboard
#Settings
#Exit




#if mouse_pos[0]>=75 and mouse_pos[0]<=260 and mouse_pos[1]>=95 and mouse_pos[1]<=300:




#if counter==0:
# display_Title("SETTINGS", WIDTH/2-text.get_width()/2, 170)
        # display_message2("Background Color")
        # display_message3("Object Color")
        # display_message4("Sound=On/Off")
        # display_message5("Screen Size")
        # py.time.delay(300)
        # py.display.update()
        # counter+=1
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
