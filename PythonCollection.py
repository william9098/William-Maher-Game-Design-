#William Maher
#9/27/21


#Challenge- try to get  user to guess to randomly pick a word, but now instead of user giving full word, we want user to guess 1 letter
#at a time.

#Four basic collection data types in Python

#List- collection which ordered and changelable allows duplicate members, list is [], [1-banana, 2- apple, 3- blueberry] 
# print(fruit[2]) going to print apple

#Tuple- collection which is ordered and unchangeable. allows duplicate members, tuple is ()

#Collection which is unordered and unindexed. No Duplicate members

#Dictionary is a colletion which is unordered, changeable and indexed. No duplicated members. good for translation games

#Python Lists-
#a list is a collection which is ordered and changeable. IN python lists are wrtitten with square brackets:
#myList=[3,6,7,8,1,2] or myFruits= ["apples', "berries"]

import random, sys, os


fruits=["apple", "grape", "olive"]

myFruit = random.choice(fruits)
myFruit=myFruit.lower()
print(myFruit)



t=('a', 'p', 'p', 'l', 'e') 
t2=('g', 'r', 'a', 'p', 'e')
t3=('o','l','i','v','e')


answer = input ("Do you want to play this game? y/n ")


while 'y' in answer:
    guessesTaken=5
    
    
    
    for x in fruits [0]:
        userInput=input("Spell out a fruit: ")
    
    if (guessesTaken== 0, userInput == t[0]):
        print("good job, you got a letter")
        guessesTaken-=1
    else:
        userInput!=t[0]
        print("wrong guess again")


    for x in fruits [1]:
        userInput=input("Spell out a fruit: ")
    if (guessesTaken== 1, userInput == t[1]):
        print("good job, you got the second letter")
        guessesTaken-=1
    else:
        userInput!=t[1]
        print("wrong guess again")



    for x in fruits [2]:
        userInput=input("Spell out a fruit: ")
    if (guessesTaken== 2, userInput == t[2]):
        print("good job, you got the third letter")
        guessesTaken-=1
    else:
        userInput!=t[2]
        print("wrong guess again")


    for x in fruits [3]:
        userInput=input("Spell out a fruit: ")
    if (guessesTaken== 3, userInput == t[3]):
        print("good job, you got the fourth letter")
        guessesTaken-=1
    else:
        userInput!=t[3]
        print("wrong guess again")


    for x in fruits [4]:
        userInput=input("Spell out a fruit: ")
    if (guessesTaken== 4, userInput == t[4]):
        print("good job, you got the fifth letter")
        guessesTaken-=1
    else:
        userInput!=t[3]
        print("wrong guess again")
    break



