#9/26/21
#William Maher

#this is a number guessing game

import random

game=True



print("The goal of this game is to guess a word, you have 10 chances to guess, I will give you hints ")
answer = input ("Do you want to play this game? y/n ")

print("This is a type of fruit")
   
while ('y' in answer):
    guessesTaken=10
    word=input ("Give me a word: ")
    print("Hint: it is a type of fruit")

    while game and guessesTaken > 0:

        word=input("Give me a word: ")
        
    if word == 'banana':
        print(" Hint: It is yellow")
        input("Give me a word: ")
        if answer== 'banana':
            print(answer.lower)
            print("Correct")
        if answer != 'banana':
            print("That is incorrect")
            print("Monke eat")


            
            












