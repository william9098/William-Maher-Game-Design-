#William Maher
#9/15/21

#game
#random number
#If(random#-guess>25)-- too high

#give user 10 chances to guess

import os

import random

playing="Do you want to play a game, press y for yes"



randy=random.randrange(1,100)
print("you have to guess a number from 1-100.")

for i in range(1,11):
    userInput=input("Give me a number: ")
print (type(userInput))
 

try:
 userInput=int(userInput)
 check=True

except ValueError:
    check=False

if(randy==userInput):
    print("You Win")
    print()

if userInput==randy:
    print("you got it!")


else:
    print("not quite...")

print(randy) 



#random(once)--> loop(1 
# input()- conditional (guess=random)