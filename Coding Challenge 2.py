#Coding Challenge 2

print("This program will enter the number of days in a given month.")

while True:
  try:
    month_Enter = int(input("Enter a month (1-12).\n>"))
  except ValueError:
    print(month_Enter, "is a invalid entry!")
  try:
    year_Enter = int(input("Enter a year.\n>"))
  except ValueError:
    print(year_Enter, "is a invalid entry!")
  
  break

if month_Enter == 1 or month_Enter == 3 or month_Enter == 5 or month_Enter == 7 or month_Enter == 8 or month_Enter == 10 or month_Enter == 12:
  print("There are 31 days in the month")
elif month_Enter == 4 or month_Enter == 6 or month_Enter == 9 or month_Enter == 11:
  print("There are 30 days in the month")
elif month_Enter == 2:
  #Hint: A year will be a leap year if it is divisible by 4 but not by 100. If a year is divisible by 4 and by 100, it is not a leap year unless it is also divisible by 400.
  if year_Enter%4 == 0 and year_Enter%100 != 0:
    leap = True
  elif year_Enter%4 == 0 and year_Enter%100 == 0 and year_Enter%400 == 0:
    leap = True
  else:
    leap = False
  
  if leap == True:
    print("There are 29 days in the month")
  elif leap == False:
    print("There are 28 days in the month")
  else:
    print("Error")
