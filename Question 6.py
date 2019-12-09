#Do question 4 recursively
def getDigits(s):
    if len(s) ==  1:
        if s.isdigit():
            return s
        else:
            return ""
    else:
        if s[0].isdigit():
            return s[0] + getDigits(s[1:])
        else:
            return "" + getDigits(s[1:])
print(getDigits("**1.23a-42"))
