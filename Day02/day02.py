colors = {
    "blue":14,
    "red":12,
    "green":13
}

def getColors(line):

    sets = [color.replace(" ","").split(",") for colors in [line.split(";")] for color in colors]

    for turn in sets:
        for cube in turn:
            for color in colors:
                pos = cube.find(color)

                if pos >=0:
                    count = int(cube[:pos])
                    if count > colors[color]:return False
                
    return True

def getMin(line):
    sets = [color.replace(" ","").split(",") for colors in [line.split(";")] for color in colors]
    blue = 0
    red = 0
    green = 0

    for turn in sets:
        pos = [(color, index[:index.find(color)]) for color in colors for index in turn if index.find(color)>=0]
        pos = dict(pos)
        if 'blue' in pos:
            blue = max(int(pos['blue']), blue)
        if 'green' in pos:
            green = max(int(pos['green']), green)
        if 'red' in pos:
            red = max(int(pos['red']), red)

    return blue*green*red

if __name__ == "__main__":
    fileInput = open("input.txt", "r")

    #1st Part

    gamesTested = [[games[0][5:], getColors(games[1])] for line in fileInput for games in [line.split(":")]]
    totalSum = sum(int(game[0]) for game in gamesTested if game[1]==True)    
    print(f'Soma dos valores: {totalSum}')

    #2nd Part

    fileInput.seek(0)
    gamesTested = [getMin(games[1]) for line in fileInput for games in [line.split(":")]]
    totalSum = sum(values for values in gamesTested)
    print(f'Soma dos valores: {totalSum}')
