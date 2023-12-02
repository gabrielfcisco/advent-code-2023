colors = {
    "blue":14,
    "red":12,
    "green":13
}

def getColors(line):

    sets = line.split(";")

    # print(sets)
    for i in sets:
        i = i.replace(" ","")
        i = i.split(",")
        for j in i:
            for color in colors:
                pos = j.find(color)

                if pos >=0:
                    count = int(j[:pos])
                    if count > colors[color]:return False

    return True

    
        

if __name__ == "__main__":
    input = open("input.txt", "r")

    gamesTested = []
    for line in input:
        # gamesTested = [[i[4:], getColors(i[1])] for i in (line.split(":"))]
        games = line.split(":")
        gamesTested.append([games[0][5:],getColors(games[1])])
        print(gamesTested)
    
    totalSum = 0
    for game in gamesTested:
        if game[1]:
            totalSum += int(game[0])
    
    print(totalSum)