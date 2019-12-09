#Coding Challenge 3

print("This program will convert distances (Inches/Miles)\nEnter (I) to convert Inches to Miles\nEnter (M) to convert Miles to Inches")
while True:
    try:
        conversion_Mode = str(input("Enter Selection: "))
    except ValueError:
        print("Please enter (I) or (M)")
    if conversion_Mode == 'I' or conversion_Mode == 'M':
        break
    else:
        print("Please enter (I) or (M)")

while True:
    try:
        distance_To_Convert = float(input("Enter distance to convert: "))
    except ValueError:
        print("Please enter a float")
    break
if conversion_Mode == 'I':
    print(distance_To_Convert, "Inches is", distance_To_Convert/63360, "Miles")
elif conversion_Mode == 'M':
    print(distance_To_Convert, "Miles is", format((distance_To_Convert*63360), '.2E'), "Inches")
else:
    print("Error")
