#9/26/21
#William Maher

#this is a word guessing game

import random,os,sys
os.system('cls')

print("The goal of this game is to guess a word, and you have 5 guesses")
answer = input ("Do you want to play this game? y/n ")


while 'y' in answer:
    guessesTaken = 5
    start = 1
    fruits=['strawberry','raspberry','blueberry']

    myFruit = random.choice(fruits)
    myFruit=myFruit.lower()
    print(myFruit)

    while start == 1 and guessesTaken>0:
        userInput=input("Give me a fruit: ")

        if(userInput == myFruit):
            print("You win!")
            start=0
        else:
            userInput != myFruit
            print("incorrect")
            guessesTaken-=1

            

    
    answer=input("Would you like to play again? ")





