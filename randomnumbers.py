#William maher
#9/15/21
#we are going to learn how to use random numbers
#make a guess number game
 
import os
import random

os.system('cls')

#this for loop was to play with random numbers


for i in range(10):
    randy = random.randint(3,5)
    print(randy)
    randy2=random.random()
    randy2 *=100
    print(int(randy2))

#arrays in python are called lists


fruits=["apple", "banana", "berries"]
myFruit= random.choice(fruits)
print(myFruit)

#give users 10 chances to get, if they are 25 numbers or more away from the goal number give them a hint, if closer no hint