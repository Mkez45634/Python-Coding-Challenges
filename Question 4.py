def getDigits(s):
    digits = ""
    if s.isdigit():
        return s
    else:
        for x in range(0, len(s)):
            if s[x].isdigit():
                digits = digits + s[x]
        return digits

print(getDigits("**1.23a-42"))
        
