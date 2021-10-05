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
import random,os

os.system('cls')

def updateWord(word, guesses): #function to update dashes and letters
    for letter in word:
        if letter in guesses:
            print(letter, end=" ")
        else:
            print('_', end = ' ')



#define function for Menu
print("You will guess a word choose a section ")
def Menu():
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
    sel=input("What would you like to do?"
    #try and excep
    sel=int(sel)
    return sel
def selWord(sel):
    if sel == 1:
        word = random.choice(fruits)
    elif sel==2:
         random.choice(compParts)
    else:
        word=random.choice(animals)
    return word

animals=["tiger, elephant"]
Fruits=["apple", "grape", "blueberry","raspberry", "banana"]

print("Guess what fruit I am thinking of. ")
name= input("What is your name? ")
counter=0
answer = input(name +" do you want to play a game y/n? ")
sel=Menu()
print(sel)
while sel !=4:
    print(name, " ,good Luck! you have 5 chances")
    turns=5
    counter +=1
    word=selWord(sel)
    word= word.lower()
    wordCount=len(word)
    letCount=0
    print(word) #just for checking our code works
    guesses=''
    updateWord(word, guesses)

    while turns>0 and letCount== wordCount : #and/ or word was guessed?, #if they returns out of turns or they guess the words they want out, so the while loop should be "and"
        print()
        newguess=input (name+ " , give me a letter: ")
        newguess= newguess.lower()
        if newguess in word:
            guesses+=newguess
            print("you guessed a letter")
        else:
            turns -=1
            print("Sorry, you have ", turns, " turns left ")

        updateWord(word, guesses)
answer=input(name + " Do you want to play again?")