#learningwhileloop

#control the main game
#instructions of the game
import random

game=True

print("The goal of this game is to guess a number from 1-100, You 6 chances to guess.")
answer = input ("Do you want to play this game? y/n ")

while('y' in answer):
    randy=random.randrange(1,100)
    guessesTaken=6
    num=input("Give me a number: ")
   #try and excepet
    while game and guessesTaken >0:
        
        num = input("Give me a number: ")

        try: 
            num=int(num)
            check=True
        except ValueError:
            check=False

        if num == randy:
            print("You won")
            game = False
        else:
            guessesTaken -=1
            
    
   
   

    print("the number was:")
    print(randy)
    answer=input("do you want to play again? y/n ")


#homework- make a game, using 2 while loops asking to guess something simmilar to this but with words
#guess a word list word ()
#no try and except



