#workshop 2
import math

while True:
  try:
    menu = int(input("\n1) Part 1\n2) Part 2\n3) Part 3\n4) Exit"))
  except ValueError:
    print("\nChoose an integer.")
  if menu == 1:
    print("\n\nPart 1")

    num = 9*2+7*2
    print("\nThe perimeter of a 9 by 7 rectangle is", str(num) + ".")

    name = str(input("\nWhat is your name"))
    print("Hello", name + ".")

    print("\nThe maximum of 5, 2, -8, 9, 5.5, 7 and 0 is", str(max(5, 2, -8, 9, 5.5, 7, 0)) + ".")

    print("\nPython is great, it's wild!")

    print("\nThe difference between Beth's age (57) and Tom's (34) is", str(57-34) + ".")

    print("\n2 to the power of 10 is", str(2**10))

    question_one_point_seven = math.factorial(7) - math.factorial(5)
    print("\nSeven factorial minus five factorial is", str(question_one_point_seven) + ".")

    print("\nIf you multiply your name 5 times you get", name*5 + ".")

    format(name, '<15')
    print("\nYour name left justified by 15 spaces looks like:")
    print(name + ".")
    print("Though strings in Python are left justified by default.")

    pi_to_five_dp = round(math.pi, 5)
    print("\nPi to five decimal places is", str(pi_to_five_dp) + ".")

    print("\nYou can't use def as a variable name to store the integer 7 as it is a keyword.")

    print("\n200 mod 12 is", str(200%7) + ".")

    print("\nYou can't store the float 7.2 as an integer, the closest you could get is to truncte it to 7.")

    unicode_encoding_name_list = []
    for x in range (0, len(name)):
      #print(x)
      #print(name[x])
      #print(ord(name[x]))
      unicode_encoding_name_list.append(ord(name[x]))
    unicode_encoding_name_string = ''.join(str(unicode_encoding_name_list))
    print("\nThe unicode encoding for your name is", str(unicode_encoding_name_string) + ".")
  elif menu == 2:
    print("\n\nPart 2")

    two_point_one_part_a ="{:.2E}".format(4580.5034)
    print("\n1a) 4580.5034 becomes", str(two_point_one_part_a))

    two_point_one_part_b ="{:.2E}".format(0.00000046004)
    print("\n1b) 0.00000046004 becomes", str(two_point_one_part_b))

    two_point_one_part_c ="{:.2E}".format(5000402.000000000006)
    print("\n1c) 5000402.000000000006 becomes", str(two_point_one_part_c))

    print("\n2a) Pi formatted to 3dp is", format(math.pi, '.3f'))

    print("\n2b) 2000.0929 formatted to 3dp with commas is", format(2000.0929, ',.3f'))

    print("\n3) John Doe\n123 Dudley Street\nWolverhampton, West Midlands, WV1 4BF")

    print("\n4a) k = 5\nnum = 0\nnum1 = num + k * 2\nnum2 = num + k * 2\nSo num is still 0 as it isn't changed during the execution of the program.")

    k = 5
    num = 0
    num1 = num + k * 2
    num2 = num + k * 2
    print("\n4b) id(num1) is", str(id(num1)), "and id(num2) is", str(id(num2)) + " so they are equal.")

    last_name = input("What is your last name?")

    age = int(input("What is your age?"))

    current_temperature = float(input("What is your current temperature in celcius?"))

    print("\n5)last_name is", str(last_name), "\nage is", str(age), "years old\ncurrent_temperature is", str(current_temperature) + " celcius.")

  elif menu == 3:
    print("\n\nPart 3")

    try:
      first_integer = int(input("\nEnter an integer.\n"))
      second_integer = int(input("\nEnter another integer.\n"))
    except ValueError:
      print("\nPlease enter an interger (whole number.")

    print("\na)", str(first_integer), "divided by", str(second_integer), "is", str(format(first_integer/second_integer, '.2f')))

    try:
      first_float = float(input("\nEnter an float.\n"))
      second_float = float(input("\nEnter another float.\n"))
    except ValueError:
      print("\nPlease enter a float (decimal number.")

    print("\nb)", str(first_float), "divided by", str(second_float), "is", str(format(first_float/second_float, '.2f')))

    try:
      first_float_c = float(input("\nEnter an float.\n"))
      second_float_c = float(input("\nEnter another float.\n"))
    except ValueError:
      print("\nPlease enter a float (decimal number.")

    print("\nc)", str(first_float_c), "divided by", str(second_float_c), "is", str("{:.2E}".format(float(format(first_float_c/second_float_c, '.2f')))))
    while True:
      try:
        utf_eight_int = int(input("\nEnter an integer between 32 and 126."))
      except ValueError:
        print("\nEnter an integer!")
      if 32 <= utf_eight_int <= 126:
        break
      else:
        print("\nPlease enter an integer between 32 and 126")#
    #print(chr(utf_eight_int))
    print("\nd)", str(utf_eight_int), "is", str(chr(utf_eight_int)))

    #+
    #-
    #*
    #/
    #//
    #%
    #**
    print("\nPart e and f.")
    integer_3_e = int(input("\nEnter an integer."))
    integer_3_e2 = int(input("\nEnter another integer."))
    print("\n3e)", str(integer_3_e), "+", str(integer_3_e2), "is", str("{:.2E}".format(float(format(integer_3_e + integer_3_e2, '.2f'))))) +".")
    print("\n", str(integer_3_e), "-", str(integer_3_e2), "is", str("{:.2E}".format(float(format(integer_3_e - integer_3_e2, '.2f'))))) +".")
    print("\n",str(integer_3_e), "*", str(integer_3_e2), "is", str("{:.2E}".format(float(format(integer_3_e * integer_3_e2, '.2f'))))) +".")
    print("\n",str(integer_3_e), "/", str(integer_3_e2), "is", str("{:.2E}".format(float(format(integer_3_e / integer_3_e2, '.2f'))))) +".")
    print("\n",str(integer_3_e), "//", str(integer_3_e2), "is", str("{:.2E}".format(float(format(integer_3_e // integer_3_e2, '.2f'))))) +".")
    print("\n",str(integer_3_e), "%", str(integer_3_e2), "is", str("{:.2E}".format(float(format(integer_3_e % integer_3_e2, '.2f'))))) +".")
    print("\n",str(integer_3_e), "**", str(integer_3_e2), "is", str("{:.2E}".format(float(format(integer_3_e ** integer_3_e2, '.2f'))))) +".")


    print("\nPart g.")

    integer_3_e = float(input("\nEnter an integer."))
    integer_3_e2 = float(input("\nEnter another integer."))
    print("\n3e)", str(integer_3_e), "+", str(integer_3_e2), "is", str("{:.2E}".format(float(format(integer_3_e + integer_3_e2, '.2f'))))) +".")
    print("\n", str(integer_3_e), "-", str(integer_3_e2), "is", str("{:.2E}".format(float(format(integer_3_e - integer_3_e2, '.2f'))))) +".")
    print("\n",str(integer_3_e), "*", str(integer_3_e2), "is", str("{:.2E}".format(float(format(integer_3_e * integer_3_e2, '.2f'))))) +".")
    print("\n",str(integer_3_e), "/", str(integer_3_e2), "is", str("{:.2E}".format(float(format(integer_3_e / integer_3_e2, '.2f'))))) +".")
    print("\n",str(integer_3_e), "//", str(integer_3_e2), "is", str("{:.2E}".format(float(format(integer_3_e // integer_3_e2, '.2f'))))) +".")
    print("\n",str(integer_3_e), "%", str(integer_3_e2), "is", str("{:.2E}".format(float(format(integer_3_e % integer_3_e2, '.2f'))))) +".")
    print("\n",str(integer_3_e), "**", str(integer_3_e2), "is", str("{:.2E}".format(float(format(integer_3_e ** integer_3_e2, '.2f'))))) +".")
  elif menu == 4:
    break
  else:
    print("Please choose an integer between 1 and 4.")