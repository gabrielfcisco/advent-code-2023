def num(line:str):
    writers = {'one':'1',
               'two':'2',
               'three':'3',
               'four':'4',
               'five':'5',
               'six':'6',
               'seven':'7',
               'eight':'8',
               'nine':'9'}
    dic = {}
    for w in writers:
        i = [
            index for index in range(len(line))
            if line.startswith(w, index)
        ]

        for j in i:
            dic[j] = writers[w]

    for n in range(0, len(line)):
        if line[n].isdigit():
            dic[n] = line[n]
    return dic

if __name__ == "__main__":
    fileInput = open("input.txt", "r")

    #1st Part
    numbers = []
    listAux = [n for n in fileInput]
    
    for n in listAux:
        numbers.append([i for i in n if i.isdigit()])

    totalSum = 0

    for n in numbers:
        totalSum += (int(n[0]+n[-1]))

    print(f'Soma dos valores: {totalSum}')

    #2nd Part
    listAux = [list(sorted(num(i).items())) for i in listAux]

    totalSum = 0

    for n in listAux:
        totalSum += (int(n[0][1]+n[-1][1]))

    print(f'Soma dos valores: {totalSum}')
