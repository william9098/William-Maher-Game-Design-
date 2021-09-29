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


fruits=["apple", "grape", "blueberry","raspberry", "banana"]
print("Word Game")
print("Guess what fruit I am thinking of. ")
name= input("What is your name? ")
counter=0
answer = input(name +" do you want to play a game y/n? ")
while 'y' in answer:
    print(name, " ,good Luck! you have 5 chances")
    turns=5
    counter +=1
    word=random.choice(fruits)
    word= word.lower()
    print(word) #just for checking our code works
    guesses=''
    for letter in word:
        if letter in guesses:
            print(letter, end=" ")
        else:
            print('_', end = ' ')
    while turns>0 and letCount==: #and/ or word was guessed?, #if they returns out of turns or they guess the words they want out, so the while loop should be "and"
        print()
        newguess=input (name+ " , give me a letter: ")
        newguess= newguess.lower()
        if newguess in word:
            guesses+=newguess
            print("you guessed a letter")
        else:
            turns -=1
            print("Sorry, you have ", turns, " turns left ")

        for letter in word:
            if letter in guesses:
                print(letter, end=" ")
            else:
                print('_', end = ' ')
answer=input(name + " Do you want to play again?")
