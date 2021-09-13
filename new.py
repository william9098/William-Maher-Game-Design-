#check it 

stars = int(input("Enter rows of stars: "))


line = stars
space = 0
stars2 = line

for i in range (line):
    for h in range (stars2):
        print( "*", end = " ")
    
    stars2 -= 1

    for j in range (space):
        print(" ", end = " ") 
    space += 2

    for counter in range (stars):
        print( "*", end = " " )

    print ()
    stars -= 1

print("so smort me")

#am absolute legend

#star + = 1