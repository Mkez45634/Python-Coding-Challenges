from random import randint
def tripleSum(List):
    index = -1
    indexSum = 0
    for x in range(1, len(List)-2):
        mysum = List[x-1] + List[x] + List[x+1]
        if mysum > indexSum:
            index = x
            indexSum = mysum
    return index

myInt = int(input("give int"))
rndList = []
for y in range(0, myInt):
    rndList.append(randint(0, myInt))
print(rndList)
print(tripleSum(rndList))



