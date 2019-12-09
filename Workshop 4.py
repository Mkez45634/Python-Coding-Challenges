#Workshop 4
menu = int(input("Enter 1, 2 or 3 for the respective part."))

if menu == 1:
    #Part 1

    #1

    total = 0
    counter = 100
    while counter <200:
        total += counter
        counter += 2
        print(counter)
    print(total)


    #2

    total_Value = 0

    while True:
        try:
            given_Value = int(input("Enter a integer, press 0 to finish adding.\n>"))
        except ValueError:
            print("Please enter a integer value.")
        if given_Value > 0 and given_Value <= 100:
            total_Value += given_Value
        elif given_Value == 0:
           break
        else:
            continue
    print("The total is " + str(total_Value) + ".")

    #3

    #see above

    #4

    neg = 0
    pos = 0

    while True:
        try:
            given_Integer = int(input("Enter a integer, press 0 to finish adding.\n>"))
        except ValueError:
            print("Please enter a integer value.")
        if given_Integer < 0:
            neg += 1
        elif given_Integer > 0:
            pos += 1
        elif given_Integer == 0:
            break
        else:
            continue
    print("Postivie numbers " + str(pos) + ".\nNegative numbers " + str(neg) + ".")

    #5
    while True:
        try:
            given_String = input("Give a string to reverse\n>")
        except ValueError:
            print("Please enter a string")

        if isinstance(given_String, basestring) == True:
            break
        else:
            continue
    #reversing the string.

    new_String = ''
    for x in range(0, len(given_String)):
        new_String.append(given_String[len(given_String - x)])
    print("Reversed is " + str(new_String) + ".")
        
elif menu == 2:

    #1
    count_100 = []
    x = 0
    y = 1

    while x < 10:
      while y < 11:
        count_100.append(x*10 + y)
        y += 1
      str_100 = ','.join([format(x, '02d') for x in count_100])
      print(str_100)
      y = 1
      count_100.clear()
      x += 1

    #2

    print()
    count_100_2 = []
    a = 0
    b = 1

    while a < 10:
      for b in range (1, 11):
        count_100_2.append(a*10 + b)
        b += 1
      str_100_2 = ','.join([format(x, '02d') for x in count_100_2])
      print(str_100_2)
      b = 1
      count_100_2.clear()
      a += 1

    #3

    product = 1
    num = int(input('Enter first number: '))# need to cast it as an integer
    while num != 0:
        if num!= 0: # need to not multiply product by 0
            product = product * num #must be before the next input, otherwise the first input is lost.
        num = int(input('Enter first number: ')) # need to cast it as an integer
        
    print('product =', product)

    #4
    #a and b is definite

elif menu == 3:

    #1
    #change = int(input("How much change should you dispence? (pennies)\n>"))
    print("Change    50p    20p    10p    5p    2p    1p")
    print("0           0      0      0     0     0     0")
    for x in range (1, 100):
        change = x
        Count50 = 0
        Count20 = 0
        Count10 = 0
        Count5 = 0
        Count2 = 0
        Count1 = 0
        while change != 0:
            if change/50 >= 1:
                change -= 50
                Count50 += 1
            elif change/50 < 1:
                if change/20 >= 1:
                    change -= 20
                    Count20 += 1
                elif change/20 < 1:
                    if change/10 >= 1:
                        change -= 10
                        Count10 += 1
                    elif change/10 < 1:
                        if change/5 >= 1:
                            change -=5
                            Count5 += 1
                        elif change/5 < 1:
                            if change/2 >= 1:
                                change -= 2
                                Count2 += 1
                            elif change/2 < 1:
                                if change/1 >= 1:
                                    change -= 1
                                    Count1 += 1
            if change == 0:
                break
    print(str(x) + "           " + str(Count50) + "      " + str(Count20) + "      " + str(Count10) + "    " + str(Count5) + "     " + str(Count2) + "    " + str(Count1) + ".")

    #2
    #calculating anagrams of words.
    alphabet_Word_One = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    alphabet_Word_Two = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    #print(len(alphabet_Word_One))
    #print(len(alphabet_Word_Two))
    #strip the letters and add 1 to the lsit in the correct spot, then compare the two and if they match it's an anagram.

    word_One = str(input(""))
    
    for x in range (0, len(
        
    
    
    
else:
    print("error")
    

