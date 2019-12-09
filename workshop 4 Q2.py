from random import randint

def reverseList(List):
    for x in range(0, (len(List) - 1)//2):
        try:
            endSpot = len(List) - 1 - x
            temp = List[x]
            List[x] = List[endSpot]
            List[endSpot] = temp
        except IndexError:
            continue
    return List

myint = int(input("Give int"))
rndList = []
for y in range(0, myint):
    rndList.append(randint(0, myint))
print(rndList)
print(reverseList(rndList))