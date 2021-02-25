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
   
    while (teams[0] >0 or teams[1] > 0 or teams[2] > 0):
        if(len(pizzas) == 0):
            break
        if(len(pizzas)<4 and teams[2] > 0):
            if(len(pizzas)< 3 and teams[1] > 0):
                if(len(pizzas) < 2 and teams[0]>0):
                    break
        perfectSocre1,perfectSocre2,perfectSocre3=-1,-1,-1
        if(teams[0] >0 and 2 <= len(pizzas)):
            tmpReuslt1,pizzas1,perfectSocre1 = calculateScore(2,ingreds,pizzas)
        if(teams[1] >0 and 3 <= len(pizzas)):
            tmpReuslt2,pizzas2,perfectSocre2 = calculateScore(3,ingreds,pizzas)
        if(teams[2] >0 and 4 <= len(pizzas)):
            tmpReuslt3,pizzas3,perfectSocre3 = calculateScore(4,ingreds,pizzas)
        if(perfectSocre1 >= perfectSocre2 and perfectSocre1 >= perfectSocre3 and perfectSocre1 >= 0 ):
            retTeam.append(tmpReuslt1)
            teams[0] = teams[0] - 1
            pizzas = pizzas1
        elif(perfectSocre2 >= perfectSocre1 and perfectSocre2 >= perfectSocre3 and perfectSocre2 >= 0):
            retTeam.append(tmpReuslt2)
            teams[1] = teams[1] - 1
            pizzas = pizzas2
        elif(perfectSocre3 >= 0):
            retTeam.append(tmpReuslt3)
            teams[2] = teams[2] - 1
            pizzas = pizzas3
    return retTeam

#select pizza with most ingreds first, then find next one with most 
#ingreds while max the score
#calculate the best combination for numberOfPeople pizza
def calculateScore(numberOfPeople, ingreds, pizzas):
    ret = []
    perfectSore = 0
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
                if sum == pizzas[pizza][0]:
                    perfectSore = perfectSore + 1
                for ing in pizzas[pizza][2]:
                    ingredsCopy[ing] = False
                ret.append(pizzas[pizza][1])
                dupPizza.remove(pizzas[pizza])
                selectedPizza = selectedPizza + 1
        pizzas = dupPizza.copy()
    return ret,dupPizza,perfectSore

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

numPizza,ingreds,teams,pizzas = readInput("a_example")
generateSub("a.txt",numPizza,ingreds,teams,pizzas)
numPizza,ingreds,teams,pizzas = readInput("b_little_bit_of_everything.in")
generateSub("b.txt",numPizza,ingreds,teams,pizzas)
# numPizza,ingreds,teams,pizzas = readInput("c_many_ingredients.in")
# generateSub("c.txt",numPizza,ingreds,teams,pizzas)
# numPizza,ingreds,teams,pizzas = readInput("d_many_pizzas.in")
# generateSub("d.txt",numPizza,ingreds,teams,pizzas)
# numPizza,ingreds,teams,pizzas = readInput("e_many_teams.in")
# generateSub("e.txt",numPizza,ingreds,teams,pizzas)