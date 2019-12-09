while True:
    try:
        nMax = int(input("Enter a odd positive integer e.g. 11:    "))
    except ValueError:
        print("Please enter an integer!")
    if nMax < 0:
        print("Please enter a positive number!")
    elif nMax % 2 == 1:
        #nMax is odd
        break
    elif nMax % 2 != 1:
        print("Please enter a odd integer!")
n = 1
while n <= nMax:
    sum1n = 0
    i = 1
    while i <= n:
        sum1n += i
        i += 2
    print('{0:3d} {1:6d}'.format(n, sum1n))
    n += 2
