#Workshop 7
#Question 1

def myFactorial(n):
    if n == 1:
        return 1
    else:
        return n*myFactorial(n-1)


print(myFactorial(5))

#Question 2
def printDigits(n):
    print(str(n)*n)
    if n >0:
        printDigits(n-1)


printDigits(5)

#Question 3
def printDigits(n):
    if n > 0:
        printDigits(n-1)
    print(str(n)*n)

printDigits(5)

#Question 4
#10,30,60...
def myFunction(n):
    if n == 1:
        return 10
    else:
        return n*10 + myFunction(n-1)

print(myFunction(4))

#Question 5
#0,1,1,2,3,5,8,13...
def Fib(n):
    if n <= 1:
        return n
    else:
        return Fib(n-1)+Fib(n-2)

x = int(input("gib num"))
for x in range (0, x):
    print(Fib(x))