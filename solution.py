#read input file
def readInput(file):
    numPizza = 0
    ingreds = {}
    pizzas = []
    teams = []
    lineIdx = 0
    with open(file) as reader:
        for line in reader:
            if lineIdx == 0:
                tmpList = line.split()
                tmpList = [int(x) for x in tmpList]
                numPizza = tmpList[0]
                teams = tmpList[1:]
            else:
                tmpList = line.split()
                pizzas.append([(int(tmpList[0])),list(tmpList[1:])])
                for i in tmpList[1:]:
                    if i not in ingreds.keys():
                        ingreds[i] = False
            lineIdx = lineIdx+1
    return numPizza,ingreds,teams,pizzas
numPizza,ingreds,teams,pizzas = readInput("a_example")

#print(numPizza)
#print(ingreds)
#print(teams)
#print(pizzas)
#ingred {"onion":true,mushroom:true....}
#pizzas[[#ingredient][onion,pepepr,olive],[#ingredient][mushroom,tomato,basil]]
#1.select team with most person first
def selectTeam(numPizza,ingreds,teams,pizzas):
    #return [[teamType,pizza1,pizza2],[teamType2,pizza3,pizza4]]
    #deliver pizza to team with most people
    #append result of calculateScore to final,result
    retTeam = []
    pizzas = sorted(pizzas, key=lambda x:x[0])
    i = len(teams)-1
    while (i > 0):
        for k in range(0, teams[i]):
            retTeam.append(calculateScore(teams[i]+2,ingreds,pizzas))
            teams[i] = teams[i] - 1
        i = i-1
    return retTeam

#select pizza with most ingreds first, then find next one with most 
#ingreds while max the score
#calculate the best combination for numberOfPeople pizza
def calculateScore(numberOfPeople, ingreds, pizzas):
    ret = []
    ingredsCopy = ingreds.copy()
    ret.append(numberOfPeople)

    for pizza in range(0, numberOfPeople):
        sum = 0
        for ing in pizzas[pizza][1]:
            sum = sum + ingredsCopy[ing]
        if sum == pizzas[pizza][0] or pizza == len(pizzas) - 1:
            for ing in pizzas[pizza][1]:
                ingredsCopy[ing] = False
            ret.append(pizza)
            del pizzas[pizza]
    return ret

#this function use to genrate submission
def generateSub():
    pass

print(selectTeam(numPizza,ingreds,teams,pizzas))

