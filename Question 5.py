#Valid name criteria:
#letter, digit & underscore only
#can't start with a digit

def isValidName(s):
    if len(s) > 0:
        if s[0].isdigit():
            return False
        else:
            for x in range(0, len(s)):
                if s[x].isalnum() == False or s[x] != "_":
                    return False
            return True
    else:
        return False

print("Valid: ")
print(isValidName("bDay"))
print(isValidName("A0"))
print(isValidName("_a_1"))
print(isValidName("_1amt"))
print(isValidName("__"))
print(isValidName("_"))
print("")
print("Invalid: ")
print(isValidName("1a"))
print(isValidName("#A"))
print(isValidName("1_a"))
print(isValidName("[a]"))
print(isValidName(" ABC"))
print(isValidName(""))
print(isValidName("A#"))
print(isValidName("A-2"))
print(isValidName("a_5+"))

                
