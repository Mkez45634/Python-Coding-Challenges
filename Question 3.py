#Question 3
def printDigits(n):
    if n > 0:
        printDigits(n-1)
    print(str(n)*n)

printDigits(5)