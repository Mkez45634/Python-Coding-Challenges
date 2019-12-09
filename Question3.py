#Question 3

import random as rnd

entrants = []
while True:
    try:
        menu = int(input("1. add entrant(s). \n2. remove entrant(s). \n3. view entrant(s). \n4. end raffle. \n>>>"))
    except ValueError:
        print("Please enter an integer!")
    if menu == 1:
        # Add entrants
        while True: # loop until all contestants have been entered
            nameFlag = True
            while nameFlag == True: # Validating Name
                try:
                    name = str(input("Enter participant name.\n "))
                except ValueError: #check that they enter a string
                    print("Please enter a string. Error code 1.")
                name = name.split(" ")
                if len(name) == 2: #check that there is a first and last name
                    if name[0].isalpha() == True and name[1].isalpha() == True: #then the name is valid!
                        print("Valid Name.")
                        nameFlag = False
                    elif name[0].isalpha() == False or name[1].isalpha == False: # name is invlaid as one half of the name isn't a string
                        print("Invalid Name. Error Code 2.")
                    else:
                        print("Error Code 4.")
                elif name[0] == "": # If sentinal value is entered, quit while loop
                    nameFlag = False
                elif len(name) != 2: # name doesn't contain first and last name, or contains middle name(s)
                    print("len(name): " + str(len(name)))
                    print("Invalid Name. Error Code 3.")

                            
            if name[0] == "":# If sentinal value is entered, quit while loop
                break

            phoneFlag = True
            while phoneFlag == True:
                try:
                    phone = int(input("Enter participant contact number.\n "))
                except ValueError: #not a int!
                    print("Please enter a integer! Error Code 5.")
                phone = str(phone)
                if phone.isdigit() == True:
                    if len(phone) == 10 or len(phone) == 11: # valid number
                        print("Valid Phone Number.")
                        phoneFlag = False
                    elif len(phone) != 10 and len(phone) != 11: #invlaid length
                        print("Invalid Phone Number. Error Code 6.")
                elif str(phone).isdigit() == False:#not a int
                    print("Please enter a int. Error Code 7.")
                    
            
            while True:# Validating EMail
                try:
                    email = str(input("Enter participant email address.\n "))
                except ValueError: # check it's a string
                    print("Please enter a valid email address. Error Code 8")
                if email.find('@hotmail.co.uk') == -1 and email.find('@gmail.co.uk') == -1: # email doesn't contain vlaid address
                    print("Please enter a valid email address. Error Code 9.")
                elif int(email.find('@hotmail.co.uk')) != -1: # hotmail email
                    break
                elif int(email.find('@gmail.co.uk')) != -1: # gmail email
                    break
            entrants.append([name, phone, email])
    elif menu == 2:
        # Remove entrants
        nameFlag = True
        while nameFlag == True: # Validating Name
            try:
                name = str(input("Enter participant name.\n "))
            except ValueError: #check that they enter a string
                print("Please enter a string. Error code 11.")
            inputName = name
            name = name.split(" ")
            if len(name) == 2: #check that there is a first and last name
                if name[0].isalpha() == True and name[1].isalpha() == True: #then the name is valid!
                    print("Valid Name.")
                    nameFlag = False
                elif name[0].isalpha() == False or name[1].isalpha == False: # name is invlaid as one half of the name isn't a string
                    print("Invalid Name. Error Code 12.")
                else:
                    print("Error Code 14.")
            elif name[0] == "": # If sentinal value is entered, quit while loop
                nameFlag = False
            elif len(name) != 2: # name doesn't contain first and last name, or contains middle name(s)
                print("len(name): " + str(len(name)))
                print("Invalid Name. Error Code 13.")
        #now we have name, we can search entrants for that name and fins ALL records with that name. Thus we can then remove them.        
        location = []
        for x in range (0, len(entrants)):
            if entrants[x][0][0] == name[0] and entrants[x][0][1] == name[1]:
                location.append(x)
        print("Found " + str(inputName) + " " + str(len(location)) + " times!")
        print("Removing!")
        for z in range (0, len(location)):
            try:
                del entrants[location[z]]
            except IndexError:
                print("\n")
        
    elif menu == 3:
        print("Name, Surname, Phone Number, Email Address.")
        for x in range (0, len(entrants)):
            print(str(entrants[x][0][0]) + ", " + str(entrants[x][0][1]) + ", " + str(entrants[x][1]) + ", " + str(entrants[x][2]) + "." )
    elif menu == 4:
        print("Competition finished!")
        try:
            winner = entrants[(rnd.randint(0, len(entrants))-1)]
        except IndexError:
            print("Error! Length is " + str(len(entrants)) + ". Error Code 10")
            winner = entrants[0]
        print("The winner is: {0}, contact number is: {1}, email address is {2}.".format((winner[0][0] + " " + winner[0][1]), winner[1], winner[2]))
        quit


    else:
        print("Please enter an integer between 1 and 4!")



