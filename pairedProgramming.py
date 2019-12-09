import random as rnd
# PART 1 - Program Welcome #
#
def DisplayWelcome():
  print("This is a game of memory! Do you think you have what it takes?! ")
  print("Please choose a difficulty level from the following: ")

# giveNums will make the randomised questions.
def giveNums(numberOfQuestions, difficulty):
  outNums = []
  if difficulty == '1': # easy #
    difficultyLvl = 10
  elif difficulty == '2': # medium #
    difficultyLvl = 100
  elif difficulty == '3': # hard #
    difficultyLvl = 1000
  for x in range (0, numberOfQuestions):
    outNums.append(rnd.randint(0, difficultyLvl))
  return outNums

# getNums will get the users answers.
def getNums(numberOfQuestions):
  inNums = []
  forLoopRange = numberOfQuestions + 1
  for x in range (1, forLoopRange):
    numsLoop = True
    while numsLoop:
      try:
        tempInput = input("Please enter number " + str(x) + "\n>")
        tempInput = int(tempInput)
      except ValueError:
        continue
      if str(tempInput).isdigit() == True:
        inNums.append(tempInput)
        numsLoop = False

  return inNums

# compareNums will check if the users answers match the question's
def compareNums(questionArray, userArray):
  compareCount = 0
  if len(questionArray) == len(userArray): #different sized arrays mean that they aren't the same
    for x in range (0, len(questionArray)):
      if questionArray[x] == userArray[x]:
        compareCount += 1
    if compareCount == len(questionArray):
      return True
    elif compareCount != len(questionArray):
      return False
  else:
    print("Compare size error!")

DisplayWelcome()

username = input(str("What is your username?\n> "))

###''''#DO VALIDATION ON USERNAME HERE'''' ##Like this?>##

removeables = ["\n",",","(",")",".","!","?",";",":","@","%","&","*","Â£","$","^","\\","/"]
## index for the removeables tuple so the user cannot use special characters in username  ##
for x in range (0,len (removeables)):
  username = username.replace(removeables[x], "")


while True:
  # User level selection #
  level_choice = input("Easy (1) : Medium (2) : Hard (3) : Quit (4)\n> ")
  # While loop to deal with incorrect inputs/ user error #
  while level_choice != '1' and level_choice != '2' and level_choice != '3' and level_choice != '4':
      level_choice = input("Invalid Entry! please input 1,2, 3 or 4: ")
  # if statements for level selection #
  if level_choice == '1':
    difficulty = '1'
    print("You have selected easy mode!")
    print (" ")
    print ("Let's do this thing!")
  elif level_choice == '2':
    difficulty = '2'
    print("You have selected medium mode!")
    print (" ")
    print ("Let's do this thing!")
  elif level_choice == '3':
    difficulty = '3'
    print("Oh! Someone wants a challenge! You have selected hard mode!")
    print (" ")
    print ("Let's do this thing!")
  elif level_choice == '4':
    print("Bye!")
    import sys
    sys.exit()
    

  #--------------------------------------------------------------------------#
  # PART 2 - File handling - Creating High Score Text documents #
  # EASY #

  while difficulty == '1':
    easy_scores = "Easy_High_Scores"
    
    try:
      easy_file = open(easy_scores + ".txt", "r")
  # this loop catches an invalid user entry on the name #
    except IOError:
      print("Please enter a valid option: ")
    try:
      if easy_file.closed == False :
        break
    except NameError:
      continue
  # now creating easy score array here #
  if difficulty == '1':
    easy_array = []
    for line in easy_file:
      line = line.replace("\n", "")
      easy_array.append(line)
    easy_file.close()
    # now to find the top 3 score's #
    highscore_easy_first = 0
    highscore_easy_second = 0
    highscore_easy_third = 0
    for counter in range (0, len(easy_array)):
      digit_easy = easy_array[counter]
      if digit_easy.isdigit():
        if int(digit_easy) > int(highscore_easy_first):
          highscore_easy_first = digit_easy
        elif int(digit_easy) < int(highscore_easy_first) and int(digit_easy) > int(highscore_easy_second):
          highscore_easy_second = digit_easy
        elif int(digit_easy) < int(highscore_easy_second) and int(digit_easy) > int(highscore_easy_third):
          highscore_easy_third = digit_easy


  # MEDIUM #
  while difficulty == '2':
    med_scores = "Medium_High_Scores"
    try:
      med_file = open(med_scores + ".txt", 'a+')
  # this loop catches an invalid user entry on the name #
    except IOError:
      print("Please enter a valid option: ")
    try:
      if med_file.closed == False :
        break
    except NameError:
      continue
  # now creating medium score array here #
  if difficulty == '2':
    med_array = []
    for line in med_file:
      line = line.replace("\n", "")
      med_array.append(line)

  # now to find the top 3 score's #
    highscore_med_first = 0
    highscore_med_second = 0
    highscore_med_third = 0
    for counter in range (0, len(med_array)):
      digit_med = med_array[counter]
      if digit_med.isdigit():
        if int(digit_med) > int(highscore_med_first):
          highscore_med_first = digit_med
        elif int(digit_med) < int(highscore_med_first) and int(digit_med) > int(highscore_med_second):
          highscore_med_second = digit_med
        elif int(digit_med) < int(highscore_med_second) and int(digit_med) > int(highscore_med_third):
          highscore_med_third = digit_med

  # HARD #
  while difficulty == '3':
    hard_scores = "Hard_High_Scores"
    try:
      hard_file = open(hard_scores + ".txt", 'a+')
  # this loop catches an invalid user entry on the name #
    except IOError:
      print("Please enter a valid option: ")
    try:
      if hard_file.closed == False :
        break
    except NameError:
      continue
  # now creating hard score array here #
  if difficulty == '3':
    hard_array = []
    for line in hard_file:
      line = line.replace("\n", "")
      hard_array.append(line)
  # now to find the top 3 score's #
    highscore_hard_first = 0
    highscore_hard_second = 0
    highscore_hard_third = 0
    for counter in range (0, len(hard_array)):
      digit_hard = hard_array[counter]
      if digit_hard.isdigit():
        if int(digit_hard) > int(highscore_hard_first):
          highscore_hard_first = digit_hard
        elif int(digit_hard) < int(highscore_hard_first) and int(digit_hard) > int(highscore_hard_second):
          highscore_hard_second = digit_hard
        elif int(digit_hard) < int(highscore_hard_second) and int(digit_hard) > int(highscore_hard_third):
          highscore_hard_third = digit_hard

  # ------------------------------------------------------------------------#
  # PART 3 - Question array's #
  score = 0
  for roundNum in range (3, 16): # gives us the number of questions we should ask (3 to 15), if they get it wrong we break the for loop. #

    # use giveNums to generate question #
    print("Question", str(roundNum-2) + ":")
    question_array = giveNums(roundNum, difficulty)
    for question_counter in range (0, len(question_array)):
      print(">", question_array[question_counter])
    entered = input("Press enter when ready to continue.")

    # clear the screen #
    for x in range (0, 50):
      print("\n")

    # use getNums to get their answer #
    user_array = getNums(roundNum)

    # use compareNums to see if they are right or wrong. #
    if compareNums(question_array, user_array) == True:
      print("Correct.")
      score += 1

    # if False break loop, if True let it loop around for the next round #
    elif compareNums(question_array, user_array) == False:
      print("Incorrect.\nThe answer was:")
      for question_counter in range (0, len(question_array)):
        print(">", question_array[question_counter]) 
      break

    # after the question have been answered, check for a new highscore, possibly update it. #
    # don't append file if they don't make a high score #
  score = str(score)
  if difficulty == '1': # easy score setter #
    while difficulty == '1':
      easy_scores = "Easy_High_Scores"
      
      try:
        easy_file = open(easy_scores + ".txt", "a+")
    # this loop catches an invalid user entry on the name #
      except IOError:
        print("Please enter a valid option: ")
      try:
        if easy_file.closed == False :
          break
      except NameError:
        continue
    if int(score) > int(highscore_easy_first):
      print("Congratulations " + username + " you are first!")
      highscore_easy_first = score
      easy_array.append(score)
      easy_array.append(username)
      easy_file.write("\n" + score )
      easy_file.write("\n" + username )
    elif int(score) < int(highscore_easy_first) and int(score) > int(highscore_easy_second):
      print("Second place!")
      highscore_easy_second = score
      easy_array.append(score)
      easy_array.append(username)
      easy_file.write("\n" + score )
      easy_file.write("\n" + username )
    elif int(score) < int(highscore_easy_second) and int(score) > int(highscore_easy_third):
      print("You came third!")
      highscore_easy_third = score
      easy_array.append(score)
      easy_array.append(username)
      easy_file.write("\n" + score )
      easy_file.write("\n" + username )
    else: # no highscore #
      print("Better luck next time.")
    easy_file.close()
    # displaying highscore's for easy #
    easy_first_name = ''
    easy_second_name = ''
    easy_third_name = ''

    for x in range (0, len(easy_array)):
      if easy_array[x] == highscore_easy_first:
        easy_first_name = easy_first_name + " " + easy_array[x+1]
      elif easy_array[x] == highscore_easy_second:
        easy_second_name = easy_second_name + " " + easy_array[x+1]
      elif easy_array[x] == highscore_easy_third:
        easy_third_name = easy_third_name + " " + easy_array[x+1]

    print("The top 3 are:")
    print("1: " + str(highscore_easy_first) + " " + easy_first_name)
    print("2: " + str(highscore_easy_second) + " " + easy_second_name)
    print("3: " + str(highscore_easy_third) + " " + easy_third_name)

  elif difficulty == '2': # med score setter #
    if int(score) > int(highscore_med_first):
      print("Congratulations " + username + " you are first!")
      highscore_med_first = score
      med_array.append(score)
      med_array.append(username)
      med_file.write("\n" + score )
      med_file.write("\n" + username )
    elif int(score) < int(highscore_med_first) and int(score) > int(highscore_med_second):
      print("Second place!")
      highscore_med_second = score
      med_array.append(score)
      med_array.append(username)
      med_file.write("\n" + score )
      med_file.write("\n" + username )
    elif int(score) < int(highscore_med_second) and int(score) > int(highscore_med_third):
      print("You came third!")
      highscore_med_third = score
      med_array.append(score)
      med_array.append(username)
      med_file.write("\n" + score )
      med_file.write("\n" + username )
    else: # no highscore #
      print("Better luck next time.")

    # displaying highscore's for med #
    med_first_name = ''
    med_second_name = ''
    med_third_name = ''

    for x in range (0, len(med_array)):
      if med_array[x] == highscore_med_first:
        med_first_name = med_first_name + " " + med_array[x+1]
      elif med_array[x] == highscore_med_second:
        med_second_name = med_second_name + " " + med_array[x+1]
      elif med_array[x] == highscore_med_third:
        med_third_name = med_third_name + " " + med_array[x+1]

    print("The top 3 are:")
    print("1: " + str(highscore_med_first) + " " + med_first_name)
    print("2: " + str(highscore_med_second) + " " + med_second_name)
    print("3: " + str(highscore_med_third) + " " + med_third_name)

  elif difficulty == '3': # hard score setter #
    if int(score) > int(highscore_hard_first):
      print("Congratulations " + username + " you are first!")
      highscore_hard_first = score
      hard_array.append(score)
      hard_array.append(username)
      hard_file.write("\n" + score )
      hard_file.write("\n" + sername )
    elif int(score) < int(highscore_hard_first) and int(score) > int(highscore_hard_second):
      print("Second place!")
      highscore_hard_second = score
      hard_array.append(score)
      hard_array.append(username)
      hard_file.write("\n" + score )
      hard_file.write("\n" + username )
    elif int(score) < int(highscore_hard_second) and int(score) > int(highscore_hard_third):
      print("You came third!")
      highscore_hard_third = score
      hard_array.append(score)
      hard_array.append(username)
      hard_file.write("\n" + score )
      hard_file.write("\n" + username )
    else: # no highscore #
      print("Better luck next time.")

    # displaying highscore's for hard #
    hard_first_name = ''
    hard_second_name = ''
    hard_third_name = ''

    for x in range (0, len(hard_array)):
      if hard_array[x] == highscore_hard_first:
        hard_first_name = hard_first_name + " " + hard_array[x+1]
      elif hard_array[x] == highscore_hard_second:
        hard_second_name = hard_second_name + " " + hard_array[x+1]
      elif hard_array[x] == highscore_hard_third:
        hard_third_name = hard_third_name + " " + hard_array[x+1]

    print("The top 3 are:")
    print("1: " + str(highscore_hard_first) + " " + hard_first_name)
    print("2: " + str(highscore_hard_second) + " " + hard_second_name)
    print("3: " + str(highscore_hard_third) + " " + hard_third_name)

  entered = input("Press enter when ready to continue.")
  for x in range (0, 50):
      print("\n")


