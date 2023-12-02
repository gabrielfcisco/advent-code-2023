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
    for word, valor in writers.items():
        indexs = [
            index for index in range(len(line))
            if line.startswith(word, index)
        ]

        for index in indexs:
            dic[index] = valor

    for index, char in enumerate(line):
        if char.isdigit():
            dic[index] = char

    return dic

if __name__ == "__main__":
    fileInput = open("input.txt", "r")

    #1st Part
    numbers = [[char for char in line if char.isdigit()] for line in fileInput ]
    totalSum = sum(int(number[0] + number[-1]) for number in numbers)

    print(f'Soma dos valores: {totalSum}')

    #2nd Part

    fileInput.seek(0)
    result = [sorted(num(line).items()) for line in fileInput]

    totalSum = sum(int(valor[0][1] + valor[-1][1]) for valor in result)

    print(f'Soma dos valores: {totalSum}')
