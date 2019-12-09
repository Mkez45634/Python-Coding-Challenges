# output n and n! for n to nMax
while True:
    try:
        nMax = int(input("Enter a  positive integer e.g. 11:    "))
    except ValueError:
        print("Please enter an integer!")
    if nMax < 0:
        print("Please enter a positive number!")
    elif nMax > 0:
        break

# validated input above

for n in range(1, nMax+1):
    nFactorial = 1
    for x in range(n, 0, -1):
        nFactorial = nFactorial * x
    print('{0:3d} {1:10d}'.format(n, nFactorial))
