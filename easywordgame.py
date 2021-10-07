#William Maher
#9/29/21 (class time) #with class
#randomly select word
#creating a list of words
#randomly selectimng word from list
#give user some turns
#show word to suer with characters
#play as long as user has turns or guessed

#figure out length of word
#add one to letter acocount
import random
import os

os.system('clear')

def updateWord(word, guesses,): #function to update dashes and letters
    for letter in word:
        if letter in guesses:
            print(letter, end=" ")
        else:
            print('_', end = "  ")



#define function for Menu

def Menu():
    print("You will guess a word choose a section ")
    print()
    print("######################################")
    #put instructions above menu
    print("#                  MENU               #")
    print("#             1. Fruits               #")
    print("#             2. Computer Parts       #")
    print("#             3. Animals              #")
    print("              4. Exit                 #")
    print(" To play the game select 1-3 to exit select 4")
    print("#######################################")
    print()
    sel=input("What would you like to do?")
    #try and except
    sel=int(sel)
    return sel

animals=["tiger, elephant"]
fruits=["apple", "grape", "blueberry","raspberry", "banana"]
compParts = ["os", "case"]

def selWord():
    if sel == 1:
        selWord = random.choice(fruits)
    elif sel==2:
        selWord = random.choice(compParts)
    else:
        selWord=random.choice(animals)
   
animals=["tiger, elephant"]
fruits=["apple", "grape", "blueberry","raspberry", "banana"]
compParts = ["os", "case"]



print("Guess what fruit I am thinking of. ")
name= input("What is your name? ")
maxScore=0 #to score highest score
answer = input(name +" do you want to play a game y/n? ")
sel=Menu()
print(sel)

while sel ==1 or sel ==2 or sel ==3:
    print(name + " ,good Luck! you have 5 chances")
   
    
    word=selWord(sel)
    word= word.lower()
    wordCount=len(word)
    turns=wordCount+2
    letCount=0 #variable to check if the user guesses the word
    print(word) #just for checking our code works
    guesses=' '
    updateWord(word, guesses)
    score=0

    while turns>0 and letCount<wordCount: #and/ or word was guessed?, #if they returns out of turns or they guess the words they want out, so the while loop should be "and"
        print()
        newguess=input (name+ " , give me a letter: ")
        newguess= newguess.lower()
        if newguess in word:
            guesses+=newguess
            print("you guessed a letter")
        else:
            turns -=1
            print("Sorry, you have ", turns, " turns left ")

     
        if sel == 1:
            print(name + ", good luck! You have 5 chances to guess my word.")
            turns=5
            word = random.choice(animals)
            word = word.lower()
            print(word)
            guesses = ' ' 
            updateWord(word, guesses)


            while turns > 0:
                print()
                newguess=input("Give me a letter: ")
                newguess=newguess.lower()
                if newguess in word:
                    guesses += newguess
                    print("You guessed one letter. ")
            else:
                turns-=1
                print("Sorry, you have ", turns, " turns left.")

        if sel == 2:
            print(name + ", good luck! You have 5 chances to guess my word.")
            turns=5
            word = random.choice(animals)
            word = word.lower()
            print(word)
            guesses = ' ' 
            updateWord(word, guesses)


            while turns > 0:
                print()
                newguess=input("Give me a letter: ")
                newguess=newguess.lower()
                if newguess in word:
                    guesses += newguess
                    print("You guessed one letter. ")
            else:
                turns-=1
                print("Sorry, you have ", turns, " turns left.")

        if sel == 3:
            print(name + ", good luck! You have 5 chances to guess my word.")
            turns=5
            word = random.choice(animals)
            word = word.lower()
            print(word)
            guesses = ' ' 
            updateWord(word, guesses)


            while turns > 0:
                print()
                newguess=input("Give me a letter: ")
                newguess=newguess.lower()
                if newguess in word:
                    guesses += newguess
                    print("You guessed one letter. ")
            else:
                turns-=1
                print("Sorry, you have ", turns, " turns left.")



    
        updateWord(word,guesses)
        os.system('cls')
        score=3*wordCount+5*turns
        if score > maxScore:
            maxScore=score
        print(maxScore)
    sel=Menu() 
        
        
        
        
        
        
        
    



#and letCount== wordCount:   



