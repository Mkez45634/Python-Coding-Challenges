#My own absolute function
import math

def myABS(n):
    if str(n).isdigit == True:
        flag = "digit"
    elif str(n).find(".") != -1:
        flag = "float"
    else: #it's a complex number
        flag = "complex"

    if flag == "digit":
        return int(n)
    elif flag == "float":
        return float(n)
    elif flag == ("complex"):

