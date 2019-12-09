#Prompts the suer for value n, then prints all positive multiples of 6 that do not exceed n
while True:
    try:
        nMax = int(input("Enter a positive integer e.g. 11:    "))
    except ValueError:
        print("Please enter an integer!")
    if nMax > 0:
        #nMax is positive and an integer
        break

for x in range(0, nMax+1, 6):
    if x != 0:
        print(x)
    
