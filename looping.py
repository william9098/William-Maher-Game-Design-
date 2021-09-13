# William Maher
#9/7/21
#We are going to learn how to use looping
#ask user for # of stars (input)
#Loop(repeat 7 times)
#print ("*")

star = int(input("how many stars? "))
#typecasting- changing type of data
#for-counter 0-7 (7 wouldnt be included in the range)

# print("stars", star)
line = star 

for i in range(line):
    #add a loop for the spaces
    for counter in range(star): #you can use number or variable #spacing below has to be three spaces out, anything not three spaces out is not going to be in the loop
        print("* ", end=" ")

    print() #print a return creating a new line
    star-=1 #short cut for star= star -1

print()
print("Thank You")


# chalenge do same task except opposite
# ****
#  ***
#   **
#    *
#should look like whats listed above
# print(counter+1, end=" ")
