# Coding Challenge 4

#The cipher using a 2d array
cipherUpper = [['A', 'M'], ['B', 'H'], ['C', 'T'], ['D','F'], ['E', 'G'], ['F', 'K'], ['G', 'B'], ['H', 'P'], ['I', 'J'], ['J', 'W'], ['K', 'E'], ['L', 'R'], ['M', 'Q'], ['N', 'S'], ['O', 'L'], ['P', 'N'], ['Q', 'I'], ['R', 'U'], ['S', 'O'], ['T', 'X'], ['U', 'Z'], ['V', 'Y'], ['W', 'V'], ['X', 'D'], ['Y', 'C'], ['Z', 'A']]
cipherLower = [['a', 'm'], ['b', 'h'], ['c', 't'], ['d', 'f'], ['e', 'g'], ['f', 'k'], ['g', 'b'], ['h', 'p'], ['i', 'j'], ['j', 'e'], ['k', 'e'], ['l', 'r'], ['m', 'q'], ['n', 's'], ['o', 'l'], ['p', 'n'], ['q', 'i'], ['r', 'u'], ['s', 'o'], ['t', 'x'], ['u', 'z'], ['v', 'y'], ['w', 'v'], ['x', 'd'], ['y', 'c'], ['z', 'a']]


#Encryption function
def encryptString(string):
    encryptionList = []
    for x in string:
        #print("x is",x)
        for y in range (0, 26):
            if x == cipherUpper[y][0]:
                #print(cipherUpper[y][1])
                encryptionList.append(cipherUpper[y][1])
            elif x == cipherLower[y][0]:
                #print(cipherLower[y][1])
                encryptionList.append(cipherLower[y][1])
    answer = ''.join(encryptionList)
    print(answer, encryptionList)
    return answer
                
#Decryption function
def decryptString(string):
    encryptionList = []
    for x in string:
        #print("x is",x)
        for y in range (0, 26):
            if x == cipherUpper[y][1]:
                #print(cipherUpper[y][1])
                encryptionList.append(cipherUpper[y][0])
            elif x == cipherLower[y][1]:
                #print(cipherLower[y][1])
                encryptionList.append(cipherLower[y][0])
    answer = ''.join(encryptionList)
    print(answer, encryptionList)
    return answer
	
#defining the main function
def myMain():

    #asking the user wehter they want to decrypt or encrypt
    while True:
        try:
            choice = str(input("Enter 'e' to encrypt or 'd' to decrypt.\n"))
        except ValueError:
            print("Please enter the letters 'e' or 'd'.\n")
        if choice != 'e' and choice != 'd':
            print("Please enter the letters 'e' or 'd'.\n")
        elif choice == 'e': #asking for the string they want to encrypt
            encrypt = str(input("Enter password: "))
            break
        elif choice == 'd': #asking for the string they want to decrypt
            decrypt = str(input("Enter password: "))
            break
    
    if choice == 'e':
        output = encryptString(encrypt)

    elif choice == 'd':
        output = decryptString(decrypt)

    print("Your password is now", output)            


myMain()
