#write our own version of MAX

from random import randint

def myMax(theList):
    theList.sort()
    return theList[len(theList) - 1]

rndList = []
myInt = int(input("give a integer!"))
for x in range(0, myInt):
    rndList.append(randint(0,myInt))
print(myMax(rndList))

