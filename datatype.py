#William Maher
#9/13/21
#how strings work
#this is about data types 


import os

os.system('cls')

#Integers:
# int
#long

#REAL:
# float (- 0 +)
#double (- 0 +)

#float uses decimal if you put 5.0, instead of 5 it will think its a float instead of a long
#integers- long (8 bytes) float (4 bytes), double (8 bytes), Boolean


#unicode acsII + extra 

userInput=(input(" type something ")) #sting - 'str'
print(type(userInput))

try:
    int(userInput)
    check=True

except ValueError:
    check=False

print(check) 

#char- 1 
#array- keeps several things together, "i am cool" is an array of characters

if(check): #boolean (if, else, etc.) #if this is true i want to print nothing
    #i'll be back
    print()
else:
    print(len(userInput)) 
for i in userInput:
    print(i)

if len(userInput>3):
    print(userInput[3])

    #for i in (word)
    #print (i, end = " ")
