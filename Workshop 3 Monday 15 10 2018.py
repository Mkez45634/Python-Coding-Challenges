#Mike Lloyd Workshop 3 Monday 15/10/2018.

#Part 2
while True:
    try:
        num = int(input("Type a integer between 0 to 200 inclusive."))
    except ValueError:
        print("Please enter an integer.")
    if num >= 0 and num <= 200:
        break
    else:
        print("Please enter a number between 0 to 200 inclusive.")
#1a)
if num >= 0 and num < 100:
    print("The number is between 0 ans 99 inclusive!")

#1b)
if num >= 0 and num < 100 or num == 200:
    print("The number is less than 100 and greater than or equal to 0, or it is equal to 200.")

#3a)
if num >= 0 and num <= 100:
    print("Within Range.")
#3b)
elif num < 0 and num > 100:
    print("Out of Range.")
else:
    print("Error")

#4)
while True:
    try:
        temperature = int(input("Input a fahrenheit temperature."))
        humidity = int(input("Input a humidity."))
        break
    except ValueError:
        print("Please enter two integers")

if temperature >= 85 and humidity > 60:
    print("Muggy day today.")
elif temperature >= 85:
    print("Warm, but not muggy today.")
elif temperature >= 65:
    print("Pleasent today.")
elif temperature <= 45:
    print("Cold day.")
else:
    print("Cool day.")


#Part 3

#1a and 1b)
while True:
    try:
        userCharacter = chr(input("Please enter A, B or C."))
    except ValueError:
        print("Please enter A, B or C.")
    if userCharacter == 'A' or userCharacter == 'B' or userCharacter == 'C':
        break
    else:
        print("Please enter A, B or C.")
        
if userCharacter == 'A':
    print("Apple.")
elif userCharacter == 'B':
    print("Banana.")
elif userCharacter == 'C':
    print("Coconut.")
else:
    print("Error")

#1c)
while True:
    try:
        creds = int(input("Please enter your Credits."))
        break
    except ValueError:
        print("Please enter a integer.")

if creds >= 90:
    print("Senior Status.")
elif creds < 90 and creds >= 60:
    print("Junior Status.")
elif creds < 60 and creds >= 30:
    print("Sophomore Status.")
else:
    print("Freshmen Status.")

#1d)
lootboxPrice_GB = 2
while True:
    try:
        num_of_lootbox = int(input("How many lootboxes would you like?"))
        break
    except ValueError:
        print("Please enter an integers")

if numb_of_lootbox > 100:
    price_total = 0.8 * num_of_lootbox * lootboxPrice_GB
elif numb_of_lootbox > 100:
    price_total = 0.9 * num_of_lootbox * lootboxPrice_GB
else:
    price_total = 1.0 * num_of_lootbox * lootboxPrice_GB

print("Your lootboxes cost", price_total, ".")

#1e)
while True:
    try:
        numb = int(input("Please enter a number."))
        break
    except ValueError:
        print("Please enter a integer.")

if numb % 5 == 0 and numb % 3 == 0:
    print("Fizz Buzz")
elif numb % 5 == 0:
    print("Buzz")
elif numb % 3 == 0:
    print ("Fizz")

#2a, 2b, 2c and 2d.)
while True:
    try:
        salary = int(input("Please enter a your yearly salary in GBP."))
        break
    except ValueError:
        print("Please enter a integer.")
if salary > 150000:
    income_tax = (0.45 * salary)

elif salary < 150000 and salary > 45000:
    if salary < 123700:
        print("Tax-free allowance is available.")
    income_tax = (0.4 * salary)
else:
    print("Tax-free allowance is available.")
    income_tax = 0.2 * salary

if salary/52 > 162:
    NI_tax_base = 0.12 * salary
    if salary/52 > 892:
        NI_tax_extra = 0.02 * (salary - (892*52))
        NI_tax_total = NI_tax_base + NI_tax_extra
    NI_tax_total = NI_tax_base
    

print("Per month income and tax:\nSalary is:", salary/12,".\nIncome tax is", income_tax/12, ".\nNational Insurance tax is", NI_tax_total/12, ".\nIncome is", (salary - income_tax - NI_tax_total)/12,".")
print("\nPer week income and tax:\nSalary is:", salary/52,".\nIncome tax is", income_tax/52, ".\nNational Insurance tax is", NI_tax_total/52, ".\nIncome is", (salary - income_tax - NI_tax_total)/52,".")   
