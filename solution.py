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
                pizzas.append([(int(tmpList[0])),lineIdx - 1,list(tmpList[1:])])
                for i in tmpList[1:]:
                    if i not in ingreds.keys():
                        ingreds[i] = True
            lineIdx = lineIdx+1
    return numPizza,ingreds,teams,pizzas


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
    pizzas = sorted(pizzas, key=lambda x:x[0],reverse=True)
    i = len(teams)-1
    #i = 0
    while (i >= len(teams)):
        for k in range(0, teams[i]):
            if(i+2 <= len(pizzas)):
                tmpReuslt,pizzas = calculateScore(i+2,ingreds,pizzas)
                retTeam.append(tmpReuslt)
                teams[i] = teams[i] - 1
            else:
                break
        i = i-1
    return retTeam

#select pizza with most ingreds first, then find next one with most 
#ingreds while max the score
#calculate the best combination for numberOfPeople pizza
def calculateScore(numberOfPeople, ingreds, pizzas):
    ret = []
    ingredsCopy = ingreds.copy()
    ret.append(numberOfPeople)
    selectedPizza = 0
    dupPizza = pizzas.copy()
    while selectedPizza < numberOfPeople:
        for pizza in range(0, len(pizzas)):
            if(selectedPizza == numberOfPeople):
                break
            sum = 0
            for ing in pizzas[pizza][2]:
                sum = sum + ingredsCopy[ing]
            if sum == pizzas[pizza][0] or pizza == len(pizzas) - 1:
                for ing in pizzas[pizza][2]:
                    ingredsCopy[ing] = False
                ret.append(pizzas[pizza][1])
                dupPizza.remove(pizzas[pizza])
                selectedPizza = selectedPizza + 1
        pizzas = dupPizza.copy()
    return ret,dupPizza

#this function use to genrate submission
def generateSub(file,numPizza,ingreds,teams,pizzas):
    result = selectTeam(numPizza,ingreds,teams,pizzas)
    f = open(file, "w")
    f.write(str(len(result)))
    f.write("\n")
    for line in result:
        for char in line:
            f.write(str(char)+" ")
        f.write("\n")
    f.close()

# numPizza,ingreds,teams,pizzas = readInput("a_example")
# generateSub("a.txt",numPizza,ingreds,teams,pizzas)
# numPizza,ingreds,teams,pizzas = readInput("b_little_bit_of_everything.in")
# generateSub("b.txt",numPizza,ingreds,teams,pizzas)
numPizza,ingreds,teams,pizzas = readInput("c_many_ingredients.in")
generateSub("c.txt",numPizza,ingreds,teams,pizzas)
# numPizza,ingreds,teams,pizzas = readInput("d_many_pizzas.in")
# generateSub("d.txt",numPizza,ingreds,teams,pizzas)
# numPizza,ingreds,teams,pizzas = readInput("e_many_teams.in")
# generateSub("e.txt",numPizza,ingreds,teams,pizzas)