
stars = int(input("Enter rows of stars: "))

line = stars
space = 0

for i in range(line):
    for j in range(space):
        print(" ", end=" ")
    space += 1

    for counter in range(stars):
        print( "*", end = " ")
    
    print()
    stars -= 1

print()


