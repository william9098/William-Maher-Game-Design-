# william
#10/7/21
#WE are going to learn how to: open() a file
#write a file 'w'
# read from a file 'r'
#append to a file 'a'
#close() close a file

import os, time
os.system('cls')
#to creat a file you must declare an object so we can open a file
# when you open a file you need to use 'w' 

myFile=open('score.txt', 'w') #here we creat the file object
myFile.write(" hi, I am william \n who are you")
#always close a file when ur done using it
myFile.close()


myFile=open('score.txt', 'w')
myFile.write(" and now we will play a game")
myFile.close()
#read and print the file
# if you want to remove what you said b4 if you use write but if you use append it doesnt

fileMy=open('score.txt', 'r')
print(fileMy.read())
fileMy.close()
score=450
anotherFile= open('score.txt','a')
anotherFile.write("\n the highest score: \t" + str(score))
anotherFile.close()

# all you have to do it when done tiwht game after find maximum game

# fileMy=open('score.txt', 'r')
# print(fileMy.read())
# fileMy.close()
# score=450
# anotherFile= open('score.txt','a')
# anotherFile.write("\n the highest score: \t" + str(score))
# anotherFile.close()
#hw now need to creat file for game for score 
#plug in
#

