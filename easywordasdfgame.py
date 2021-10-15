import random, os
os.system('cls')

def updateWord(word, guesses): #Function to update dashes
    for letter in word:
        if letter in guesses:
            print(letter, end=" ")
        else:
            print('_', end= " ")
#define function for menu
def Menu():
    print()
    print("You have to guess a word, the type of word is provided below")
    print()
    print("###############################")
    print("          ----Menu----         ")
    print(                                 )
    print("           1. Animals          ")
    print("           2. Computer Parts         ")
    print("           3. Fruits         ")
    print("           4. Scoreboard    ")
    print("           5. Leave            ")        
    print()
    print("############################")
    print("To play the game, select 1-3 and to exit select 4.")
    print()
    sel=input("What would you like to do? ")
    #Put in try and except here
    sel=int(sel)
    return sel

def selWord():
    if sel == 1:
        word= random.choice(animals)
    elif sel == 2:
        word= random.choice(compParts)
    else:
        word= random.choice(fruits)

animals=["tiger", "elephant", "lion"]
fruits=["apple", "strawberry", "blueberry"]
compParts=["keyboard", "monitor", "case", "mouse"]
name= input("What is your name? ")
maxScore=100
sel = Menu()

def leave():
    if sel==5:
        print("bye")
    os._leave()



if sel == 4:
    myFile=open('score.txt', 'r')
    print(myFile.read)()
    myFile.close()


def wordSelect():
    if sel ==1:
        word=random.choice(animals)
    if sel ==2:
        word= random.choice(compParts)
    if sel ==3:
        word = random.choice(fruits)
    return word

while sel !=5 and sel!=4:
    #call function her to choose word
    word=wordSelect()
    
    word = word.lower()
    wordCount=len(word)
    turns=wordCount+2
    score=0
    print(word) #Just for checking our code, remove later.
    guesses = '' 
    updateWord(word, guesses)

    while turns > 0:
        newguess=input("Give me a letter: ")
        newguess=newguess.lower()
        if newguess in word:
            guesses += newguess
            print("You guessed one letter. ")
        else:
            turns-=1
            print("Sorry, you have ", turns, " turns left.")
            updateWord(word, guesses)    
    
    
    

    os.system('cls')
    score=3*wordCount+5*turns
    if score > maxScore:
        maxScore=score
    print(maxScore)
myFile=open('score.txt','r')
name + "\t Highest score:\t"+ str(maxScore) # line 103 and 104 need to be put into exit fucntin
sel=Menu()