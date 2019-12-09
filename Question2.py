#Question 2

#Part A
while True:
    try:
        numPeopleA = int(input("Enter the number of people."))
    except ValueError:
        print("Please enter an integer!")
    if str(numPeopleA).isdigit() == True:
        break
while True:
    try:
        numPizzaA = int(input("Enter the number of pizzas."))
    except ValueError:
        print("Please enter an integer!")
    if str(numPizzaA).isdigit() == True:
        break
while True:
    try:
        numSlicesA = int(input("Enter the number of slices per pizza."))
    except ValueError:
        print("Please enter an integer!")
    if str(numSlicesA).isdigit() == True:
        break


totalSlicesA = numSlicesA*numPizzaA

if totalSlicesA%numPeopleA == 0:
    #no leftover slices
    print("Each person gets " + str(int(totalSlicesA/numPeopleA)) + " slices.")
else:
    #there are leftover slices
    print("Each person gets " + str(int((totalSlicesA/numPeopleA)-((totalSlicesA%numPeopleA)/numPeopleA))) + " slices.")
    print("There are " + str(totalSlicesA%numPeopleA) + " leftover slices.")

#Part B
print("\nPart B\n")
while True:
    try:
        numPeopleB= int(input("Enter the number of people."))
    except ValueError:
        print("Please enter an integer!")
    if str(numPeopleB).isdigit() == True:
        break
while True:
    try:
        numPizzaB = int(input("Enter the number of pizzas."))
    except ValueError:
        print("Please enter an integer!")
    if str(numPizzaB).isdigit() == True:
        break
while True:
    sizeChoice = int(input("1. Small \n2. Medium \n3. Large \n4. Extra Large \n Please choose a size."))
    if sizeChoice != 1 and sizeChoice != 2 and sizeChoice != 3 and sizeChoice != 4:
        print("Please choose a number between 1 and 4 (inclusive).")
    elif sizeChoice == 1 or sizeChoice == 2 or sizeChoice == 3 or sizeChoice == 4:
        break

if sizeChoice == 1:
    totalSlicesB = numPizzaB*4
elif sizeChoice == 2:
    totalSlicesB = numPizzaB*8
elif sizeChoiceB == 3:
    totalSlicesB = numPizzaB*12
elif sizeChoiceB == 4:
    totalSlicesB = numPizzaB*15

if totalSlicesB%numPeopleB == 0:
    #no leftover slices
    print("Each person gets " + str(int(totalSlicesB/numPeopleB)) + " slices.")
else:
    #there are leftover slices
    print("Each person gets " + str(int((totalSlicesB/numPeopleB)-((totalSlicesB%numPeopleB)/numPeopleB))) + " slices.")
    print("There are " + str(totalSlicesB%numPeopleB) + " leftover slices.")

#Part C    
    
    
