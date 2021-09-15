#William Maher
#9/14/21

userInput=(input(" type something "))
print(type(userInput))

try:
    int(userInput)
    check=True

except ValueError:
    check=False



#str- string 
#char- 1 
#array- keeps several things together, "i am cool" is an array of characters

if(check):
    #i'll be back
    print()
else:
    print(len(userInput))


# convert 'str' to int



var1=int(input("Type your first number: "))
var2=int(input("Type your second number"))
#second number will be subtracted fromt he first

addanswer= var1 + var2
print("Addition answer:", addanswer)

subtanswer= var1 - var2
print("Subtraction answer:", subtanswer)

multanswer=var1*var2
print("Multiplication answer:", multanswer)

divanswer=var1/var2
print("Division answer:", divanswer)

modanswer = var1%var2
print("Modulus answer:", modanswer)
print("the modulus tells you the remainder between the two numbers")


